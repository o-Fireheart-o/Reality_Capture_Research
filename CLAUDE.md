# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 이 저장소의 성격

코드 저장소가 아니라 **리서치·문서 저장소**다. 빌드·테스트·린트 명령이 없고 앞으로도 없다.
산출물은 전부 한국어 마크다운 문서이며, 작업 단위는 "커밋 가능한 문서 한 편"이다.

목적: 사용자가 "Cupix의 주력사업"으로 규정한 **Reality Capture** 분야를 심층 학습하고,
그 결과를 재사용 가능한 문서로 남긴다.

## 핵심 연구 질문

모든 문서는 아래 다섯 질문 중 하나에 답하기 위해 존재한다. 질문에 답하지 않는 내용은 넣지 않는다.

1. 세상에는 어떤 Reality Capture 도구들이 있는가
2. Reality Capture는 어떤 역사를 가지고 있으며 현재 어떻게 발전해 가고 있는가
3. Reality Capture는 현 시대에 어떻게 사용되고 있는가
4. Reality Capture 기술과 연계할 수 있는 기술은 어떤 것이 있는가
5. 한 가지 기술만으로는 발전하기 어려운 시대에, 무엇을 더 배워야 발전할 수 있는가

## 파일 규약

```
docs/00-glossary.md          용어 정의 (한 용어는 여기서 한 번만 정의)
docs/01-tools.md             질문 1
docs/02-history.md           질문 2
docs/03-use-cases.md         질문 3
docs/04-adjacent-tech.md     질문 4
docs/05-learning-roadmap.md  질문 5
```

- 파일명 앞의 번호가 읽는 순서다. 새 문서를 끼워 넣을 때도 번호 체계를 유지한다.
- 문서가 길어지면 `docs/01-tools/` 처럼 디렉터리로 쪼개되, 상위에 인덱스 문서를 남긴다.
- 원문 PDF·이미지 등 첨부 자료는 `sources/` 에 둔다. 웹 링크만 있으면 별도 파일을 만들지 않는다.
- `site/index.html`은 여섯 문서를 한 장으로 묶은 웹 요약본이다. `site/_0*.html` 조각을 이어 붙여 만들고
  (`cat site/_0*.html > site/index.html`), 용어집 조각 `_07`은 `00-glossary.md`에서 `python tools/gen_glossary.py docs/00-glossary.md site/_07-glossary.html`로 생성한다. 원문과 다르면 원문이 기준이다.
  공개 주소(GitHub Pages, master push 시 자동 배포): https://o-fireheart-o.github.io/Reality_Capture_Research/
  Claude 아티팩트(비공개): https://claude.ai/artifact/LMe3sYRx6MyJb9ovYFnKaT

## 작성 규약

- 문서 상단에 `작성일` / `최종수정일`을 남긴다. 웹에서 얻은 사실은 빠르게 낡으므로 날짜가 곧 신뢰도다.
- **사실 주장에는 출처 URL과 확인 날짜를 붙인다.** 출처 없이 쓴 문장은 추측으로 간주하고 "(추정)"으로 표시한다.
- 벤더 마케팅 문구와 실제 검증된 성능을 구분해서 쓴다. 스펙 수치는 출처가 벤더인지 제3자 벤치마크인지 명시한다.
- 용어는 `00-glossary.md`에 한 번 정의하고, 다른 문서에서는 링크만 건다.
- 문서를 쓴 뒤 `korean-skills:grammar-checker`와 `korean-skills:style-guide` 스킬로 검토한다.
  AI 문체가 두드러지면 `korean-skills:humanizer`를 함께 돌린다.

## 리서치 워크플로우

- `WebSearch` / `WebFetch`가 도구 목록에 보이지 않으면 `ToolSearch`로 `select:WebSearch,WebFetch`를 먼저 불러온다.
- 조사는 넓게, 기록은 좁게. 검색 결과를 그대로 옮기지 말고 질문에 답하는 형태로 재구성한다.
- 문서 하나가 "완료"되려면: (a) 담당 질문에 답했고, (b) 주요 주장에 출처가 있고, (c) 한국어 검토를 거쳤다.

## 문서 로드맵

| 문서 | 담당 질문 | 상태 |
|------|-----------|------|
| `00-glossary.md` | 공통 | 완료 (69개 용어, 7개 문서 병합) |
| `01-tools.md` | 1 | 완료 |
| `01-tools/colmap.md` | 1 (도구 심층) | 완료 |
| `02-history.md` | 2 | 완료 |
| `03-use-cases.md` | 3 | 완료 |
| `04-adjacent-tech.md` | 4 | 완료 |
| `05-learning-roadmap.md` | 5 | 완료 |

문서 상태가 바뀌면 이 표를 갱신한다.

작성 순서는 `02 → 01 → 03 → 04 → 05`를 권장한다. 역사를 먼저 훑으면 도구 목록을 분류할 어휘가 생기고,
4번(연계 기술)은 1~3번의 결과 위에서만 판단할 수 있으며, 5번(학습 로드맵)은 반드시 마지막이다.

**01번 문서에서 먼저 결정할 것:** Reality Capture의 범위를 어디까지로 잡을지.
사진측량(photogrammetry), 지상·모바일 LiDAR, 360 이미징, 드론, SLAM, NeRF/3DGS까지 폭이 넓다.
전 산업을 훑을지, 건설·AEC 관점으로 좁힐지를 정하고 그 결정을 문서에 명시한다.
