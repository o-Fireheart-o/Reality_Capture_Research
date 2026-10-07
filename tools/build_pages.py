"""docs/*.md 를 문서별 HTML 페이지(site/pages/)로 빌드한다.

    python tools/build_pages.py

- 원문은 docs/ 의 마크다운이다. 이 스크립트는 원문을 고치지 않는다.
- 그림은 site/pages/figures/<slug>.json 매니페스트를 따라 끼워 넣는다.
  SVG는 페이지 색 토큰(var(--near) 등)을 쓰므로 인라인으로 넣는다.
"""
import html
import json
import re
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
OUT = ROOT / 'site' / 'pages'
FIG = OUT / 'figures'
REPO = 'https://github.com/o-Fireheart-o/Reality_Capture_Research/blob/master/docs/'

PAGES = [  # (원문 경로, 목차에 쓸 짧은 이름)
    ('00-glossary.md', '00 · 용어집'),
    ('01-tools.md', '01 · 도구 지형도'),
    ('01-tools/colmap.md', '01 심층 · COLMAP'),
    ('02-history.md', '02 · 역사와 진행 방향'),
    ('03-use-cases.md', '03 · 현재의 쓰임새'),
    ('04-adjacent-tech.md', '04 · 연계 기술 지도'),
    ('05-learning-roadmap.md', '05 · 학습 로드맵'),
]
META_KEYS = ('작성일', '최종수정일', '담당 질문', '상위 문서')

URL_RE = re.compile(r'(?<![(<\[="\'`])(https?://[^\s<>()\[\]`]+[^\s<>()\[\]`.,;:\'"])')


def autolink(md):
    """맨 URL을 <url> 자동 링크로 감싼다. 코드 블록과 인라인 코드는 건드리지 않는다."""
    out, fence = [], False
    for line in md.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
        if fence or line.lstrip().startswith('```'):
            out.append(line)
            continue
        parts = re.split(r'(`[^`]*`)', line)
        parts = [p if p.startswith('`') else URL_RE.sub(r'<\1>', p) for p in parts]
        out.append(''.join(parts))
    return '\n'.join(out)


def split_meta(md):
    """제목(h1)과 작성일 등 머리 정보를 떼어 낸다."""
    lines = md.split('\n')
    title, meta, body = '', [], []
    for i, line in enumerate(lines):
        s = line.strip()
        if not title and s.startswith('# '):
            title = s[2:].strip()
            continue
        if i < 15 and any(s.startswith(k + ':') for k in META_KEYS):
            k, v = s.split(':', 1)
            meta.append((k.strip(), v.strip()))
            continue
        body.append(line)
    return title, meta, '\n'.join(body)


def figure_html(fig, rel_root):
    cap = fig.get('caption', '')
    if 'svg' in fig:
        svg = (FIG / fig['svg']).read_text(encoding='utf-8')
        svg = '\n'.join(l for l in svg.split('\n') if l.strip())  # 빈 줄이 있으면 raw HTML 블록이 끊긴다
        wide = ' wide' if fig.get('wide', True) else ''
        body = f'<div class="fig-box{wide}">{svg}</div>'
        cls = ''
    else:
        src = rel_root + 'img/' + fig['img']
        alt = html.escape(fig.get('alt', ''), quote=True)
        body = f'<div class="fig-box"><img src="{src}" alt="{alt}" loading="lazy"></div>'
        cls = ' class="photo"'
    if 'img' in fig and not fig.get('credit'):
        side = OUT / 'img' / (Path(fig['img']).stem + '.json')
        fig['credit'] = json.loads(side.read_text(encoding='utf-8'))['credit']  # 사진은 출처 표기 없이 넣지 않는다
    credit = f'<span class="credit">{fig["credit"]}</span>' if fig.get('credit') else ''
    return (f'<figure{cls}>{body}<figcaption><span class="fig-label">그림 {{{{FIGNUM}}}}</span>'
            f'{cap}{credit}</figcaption></figure>')


def inject_figures(md, figs, rel_root):
    """매니페스트의 각 그림을 'after' 제목 아래, skip 개 블록 뒤에 넣는다."""
    blocks = re.split(r'\n\s*\n', md)
    inserts = {}
    for fig in figs:
        target = fig['after']
        idx = next((i for i, b in enumerate(blocks)
                    if b.lstrip().startswith('#') and target in b.split('\n')[0]), None)
        if idx is None:
            raise SystemExit(f'그림 위치를 찾지 못함: {target!r}')
        pos = idx + fig.get('skip', 1)
        inserts.setdefault(pos, []).append(figure_html(fig, rel_root))
    out = []
    for i, b in enumerate(blocks):
        out.append(b)
        out.extend(inserts.get(i, []))
    return '\n\n'.join(out)


def glossary_breaks(md):
    """용어집: 용어 줄 뒤와 출처(URL, →) 줄 앞에서만 줄을 바꾼다. 정의 문장의 원문 줄바꿈은 이어 붙인다."""
    lines = md.split('\n')
    for i, line in enumerate(lines[:-1]):
        nxt = lines[i + 1].strip()
        if not line.strip() or not nxt:
            continue
        if re.match(r'^\*\*.+\*\*$', line.strip()) or nxt.startswith(('http', '→')):
            lines[i] = line.rstrip() + '  '
    return '\n'.join(lines)


def post(htm, depth):
    # 내부 .md 링크 → .html
    htm = re.sub(r'href="(?!https?:)([^"#]+)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', htm)
    # (추정) 강조
    # SVG 안의 <text>에 span을 넣으면 도식이 깨지므로 SVG 블록은 건너뛴다
    parts = re.split(r'(<svg\b.*?</svg>)', htm, flags=re.S)
    def est(p):
        # **(추정)** 처럼 표시 자체만 굵게 쓴 경우에만 strong을 벗긴다. 앞 문장의 </strong>을 먹으면 안 된다
        p = re.sub(r'<strong>\((추정[^)<]*)\)</strong>', r'<span class="est">(\1)</span>', p)
        return re.sub(r'(?<!class="est">)\((추정[^)<]*)\)', r'<span class="est">(\1)</span>', p)
    htm = ''.join(p if p.startswith('<svg') else est(p) for p in parts)
    # 표는 가로 스크롤 상자에 넣는다(휴대폰에서 페이지가 옆으로 밀리지 않게)
    htm = re.sub(r'<table>(.*?)</table>', lambda m: '<div class="tbl-wrap"><table>' + m.group(1) + '</table></div>', htm, flags=re.S)
    # 그림 번호
    n = iter(range(1, 1000))
    htm = re.sub(r'\{\{FIGNUM\}\}', lambda m: str(next(n)), htm)
    # 외부 링크는 새 탭
    htm = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', htm)
    return htm


TEMPLATE = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Song+Myung&family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<div class="wrap">
<nav class="nav" aria-label="목차">
  <div class="nav-brand">리서치 노트 · 2026</div>
  <div class="nav-title"><a href="{root}../index.html" style="color:inherit;text-decoration:none">Reality Capture 지형도</a></div>
  <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navList">목차 열기</button>
  <ul class="nav-list" id="navList">
{pages}
    <li class="toc-title">이 문서</li>
{toc}
  </ul>
  <div class="nav-foot">원문: <a href="{src}" target="_blank" rel="noopener">{src_name}</a><br>한 장 요약: <a href="{root}../index.html">요약 페이지</a></div>
</nav>
<main class="main">
<div class="col doc">
<header class="mast">
  <div class="eyebrow">Reality Capture 심층 리서치 · 문서</div>
  <h1>{title}</h1>
  <div class="doc-meta">{meta}</div>
</header>
{body}
<div class="pager">{prev}{next}</div>
<footer class="foot">이 페이지는 <a href="{src}" target="_blank" rel="noopener">docs/{src_name}</a>에서 자동으로 만들었습니다. 내용이 다르면 원문이 기준입니다.</footer>
</div>
</main>
</div>
<script>
(function(){{
  var b=document.getElementById('navToggle'), l=document.getElementById('navList');
  function set(o){{l.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'목차 닫기':'목차 열기';}}
  b.addEventListener('click',function(){{set(!l.classList.contains('open'));}});
  l.addEventListener('click',function(e){{if(e.target.closest('a'))set(false);}});
}})();
</script>
</body>
</html>
'''


def build(only=None):
    outs = [(p, label, Path(p).with_suffix('.html')) for p, label in PAGES]
    for i, (src, label, dst) in enumerate(outs):
        if only and Path(src).stem != only:
            continue
        depth = len(Path(src).parts) - 1
        root = '../' * depth
        md = (DOCS / src).read_text(encoding='utf-8')
        title, meta, body = split_meta(md)
        slug = Path(src).stem
        mf = FIG / f'{slug}.json'
        if mf.exists():
            body = inject_figures(body, json.loads(mf.read_text(encoding='utf-8')), root)
        body = autolink(body)
        exts = ['tables', 'fenced_code', 'attr_list', 'sane_lists', 'toc']
        if slug == '00-glossary':
            body = glossary_breaks(body)
        conv = markdown.Markdown(extensions=exts, extension_configs={
            'toc': {'slugify': slugify_unicode, 'toc_depth': '2'}})
        htm = post(conv.convert(body), depth)
        toc = '\n'.join(f'    <li><a class="nav-sub" href="#{t["id"]}">{t["name"]}</a></li>'
                        for t in conv.toc_tokens)
        cur = ' aria-current="page"'
        pages = '\n'.join(
            f'    <li><a class="pg{" cur" if j == i else ""}" href="{root}{d.as_posix()}"{cur if j == i else ""}><span>{html.escape(lb)}</span></a></li>'
            for j, (_, lb, d) in enumerate(outs))
        meta_html = ''.join(f'<span>{html.escape(k)} {html.escape(v)}</span>' for k, v in meta
                            if k in ('작성일', '최종수정일'))
        prev = (f'<a href="{root}{outs[i-1][2].as_posix()}">← {html.escape(outs[i-1][1])}</a>'
                if i > 0 else '<span></span>')
        nxt = (f'<a href="{root}{outs[i+1][2].as_posix()}">{html.escape(outs[i+1][1])} →</a>'
               if i + 1 < len(outs) else '<span></span>')
        page = TEMPLATE.format(title=html.escape(title), root=root, pages=pages, toc=toc,
                               src=REPO + src, src_name=src, meta=meta_html, body=htm,
                               prev=prev, next=nxt)
        target = OUT / dst
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding='utf-8', newline='\n')
        ids = re.findall(r'<h[2-4] id="([^"]*)"', htm)
        dup = {x for x in ids if ids.count(x) > 1}
        print(f'{dst.as_posix():32} figs={htm.count("<figure")} h2={len(conv.toc_tokens)}'
              + (f' DUP-IDS={sorted(dup)}' if dup else ''))


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    build(sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--only' else None)
