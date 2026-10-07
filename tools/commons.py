"""Wikimedia Commons 사진 검색·내려받기 도구.

    python tools/commons.py search "terrestrial laser scanner"
    python tools/commons.py get "File:Leica ScanStation.jpg" leica-scanstation

get 은 라이선스를 확인해(CC0/PD/CC BY/CC BY-SA만 허용) 1600px JPEG로 줄여
site/pages/img/<이름>.jpg 에 저장하고, 출처·저작자·라이선스를 <이름>.json 에 기록한다.
내려받은 원본은 임시 디렉터리에서만 다루고 PIL로 검증한다.
"""
import html
import io
import json
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'site' / 'pages' / 'img'
API = 'https://commons.wikimedia.org/w/api.php'
UA = {'User-Agent': 'RealityCaptureResearch/1.0 (https://github.com/o-Fireheart-o/Reality_Capture_Research)'}
ALLOWED = re.compile(r'^(CC0|Public domain|PD|CC BY(-SA)? \d|CC BY(-SA)?$|Attribution)', re.I)


def api(**params):
    params.update(format='json', formatversion='2')
    url = API + '?' + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.load(r)


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()


def search(q, n=12):
    d = api(action='query', generator='search', gsrsearch=f'filetype:bitmap {q}', gsrnamespace=6,
            gsrlimit=n, prop='imageinfo', iiprop='extmetadata|size')
    for p in d.get('query', {}).get('pages', []):
        ii = p['imageinfo'][0]
        m = ii.get('extmetadata', {})
        lic = m.get('LicenseShortName', {}).get('value', '?')
        print(f"{p['title']} | {ii.get('width')}x{ii.get('height')} | {lic} | "
              f"{strip_tags(m.get('ImageDescription', {}).get('value', ''))[:90]}")


def get(title, name, width=1600):
    d = api(action='query', titles=title, prop='imageinfo',
            iiprop='url|extmetadata', iiurlwidth=width)
    p = d['query']['pages'][0]
    if 'imageinfo' not in p:
        raise SystemExit(f'없는 파일: {title}')
    ii = p['imageinfo'][0]
    m = ii['extmetadata']
    lic = m.get('LicenseShortName', {}).get('value', '')
    if not ALLOWED.search(lic) or re.search(r'\bNC\b|\bND\b', lic):
        raise SystemExit(f'허용하지 않는 라이선스: {lic} ({title})')
    artist = strip_tags(m.get('Artist', {}).get('value', '')) or '작자 미상'
    lic_url = m.get('LicenseUrl', {}).get('value', '')
    src = ii.get('thumburl') or ii['url']
    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / 'download.bin'
        with urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=60) as r:
            raw.write_bytes(r.read())
        Image.open(raw).verify()  # HTML 오류 페이지가 이미지로 저장되는 경우를 걸러 낸다
        im = Image.open(raw)
        im = im.convert('RGB')
        im.thumbnail((width, width))
        IMG.mkdir(parents=True, exist_ok=True)
        out = IMG / f'{name}.jpg'
        im.save(out, 'JPEG', quality=80, optimize=True, progressive=True)
    page = ii['descriptionurl']
    meta = {
        'title': title, 'page': page, 'artist': artist, 'license': lic, 'license_url': lic_url,
        'credit': (f'사진: {html.escape(artist)} · <a href="{page}">Wikimedia Commons</a> · '
                   + (f'<a href="{lic_url}">{html.escape(lic)}</a>' if lic_url else html.escape(lic))),
    }
    # 병렬로 받아도 충돌하지 않게 사진마다 옆에 출처 파일을 둔다
    (IMG / f'{name}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    print(f'saved {out.name} {im.size} {lic} — {artist[:60]}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    cmd = sys.argv[1]
    if cmd == 'search':
        search(' '.join(sys.argv[2:]))
    elif cmd == 'get':
        get(sys.argv[2], sys.argv[3])
