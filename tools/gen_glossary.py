import re, sys, html
from urllib.parse import urlparse

src, out = sys.argv[1], sys.argv[2]
lines = open(src, encoding='utf-8').read().splitlines()

DOC_ANCHOR = {'01-tools.md': 'tools', '02-history.md': 'history', '03-use-cases.md': 'usecases',
              '04-adjacent-tech.md': 'adjacent', '05-learning-roadmap.md': 'roadmap'}
DOC_LABEL = {'tools': '01장', 'history': '02장', 'usecases': '03장', 'adjacent': '04장', 'roadmap': '05장'}

def chip_for(url):
    h = urlparse(url).netloc.lower()
    if any(k in h for k in ('arxiv.org', 'doi.org', 'isprs', 'copernicus', 'sciencedirect', 'springer', 'wiley', 'mdpi', 'ncbi.nlm', 'semanticscholar', 'ieee')):
        return '<span class="chip ac">학술</span>'
    if any(k in h for k in ('iso.org', 'ogc.org', 'buildingsmart', 'astm.org')):
        return '<span class="chip st">표준</span>'
    if h.endswith('.go.kr') or h.endswith('.gov'):
        return '<span class="chip pb">공공</span>'
    return ''

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    return s

groups, cur, term = [], None, None
ESTIMATE = re.compile(r'\s*\*\*\(추정[^)]*\)\*\*|\s*\(추정[^)]*\)')

def refs(line):
    out = []
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)([^\[]*)', line):
        f = m.group(2).split('#')[0]
        a = DOC_ANCHOR.get(f)
        if a:
            extra = m.group(3).strip(' ,')
            out.append(f'<a href="#{a}">{DOC_LABEL[a]}{(" " + html.escape(extra)) if extra else ""}</a>')
    return out

in_body = False
for raw in lines:
    line = raw.strip()
    m = re.match(r'^##\s+\d+\.\s+(.+)$', line)
    if m:
        cur = {'name': m.group(1), 'terms': []}; groups.append(cur); term = None; in_body = True
        continue
    if not in_body or cur is None:
        continue
    if line == '---' or not line:
        if not line and term is None: pass
        continue
    tm = re.match(r'^\*\*(.+)\*\*$', line)
    if tm and '(추정' not in tm.group(1):
        term = {'t': tm.group(1), 'd': [], 'urls': [], 'refs': [], 'est': False}
        cur['terms'].append(term); continue
    if term is None:
        continue  # group intro prose
    if line.startswith('http'):
        term['urls'].append(line.split()[0]); continue
    if line.startswith('→'):
        term['refs'] += refs(line); continue
    if ESTIMATE.search(line):
        term['est'] = True; line = ESTIMATE.sub('', line)
    if '→' in line:
        line, tail = line.split('→', 1); term['refs'] += refs(tail)
    term['d'].append(line.strip())

n = 0
parts = ['<section id="glossary">',
         '  <div class="sec-head"><span class="sec-num">부록</span><h2>용어집</h2></div>',
         '  <p>여섯 문서에 나오는 용어를 한곳에 모았습니다. 각 용어는 여기서 한 번만 정의하고, 본문에서는 이 용어집을 기준으로 씁니다. 정의 뒤 링크는 그 정의의 근거입니다.</p>',
         '  <label for="glFilter" class="src" style="display:block;margin-top:18px">용어 찾기</label>',
         '  <input id="glFilter" class="gl-filter" type="search" placeholder="예: 번들조정, LOA, SLAM" autocomplete="off">',
         '  <p class="src" id="glEmpty" hidden>일치하는 용어가 없습니다. 한글 또는 영문 약어로 다시 찾아 보세요.</p>',
         '  <div class="gl">']
for g in groups:
    if not g['terms']: continue
    parts.append(f'    <div class="gl-group">\n      <h3>{html.escape(g["name"])}</h3>\n      <dl>')
    for t in g['terms']:
        n += 1
        d = inline(' '.join(t['d']))
        bits = []
        if t['est']: bits.append('<span class="chip es">추정</span>')
        for u in t['urls']:
            host = urlparse(u).netloc.replace('www.', '')
            c = chip_for(u)
            bits.append(f'<a href="{html.escape(u)}">{html.escape(host)}</a>' + (f' {c}' if c else ''))
        bits += [f'→ {r}' for r in t['refs']]
        src_line = f'<span class="src" style="display:block;margin-top:4px">{" · ".join(bits)}</span>' if bits else ''
        parts.append(f'        <div class="gl-item"><dt>{inline(t["t"])}</dt><dd>{d}{src_line}</dd></div>')
    parts.append('      </dl>\n    </div>')
parts += ['  </div>', '</section>', '']
open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(parts))
print('terms', n, 'groups', len([g for g in groups if g['terms']]))
