# Reality Capture Research

Reality Capture 분야를 다섯 개의 연구 질문으로 나눠 조사한 한국어 리서치 문서 모음입니다.
사진측량, 지상·모바일 LiDAR, 360 이미징, 드론, SLAM, NeRF/3DGS까지 전 산업을 훑되 건설·AEC를 주 렌즈로 삼았습니다.

## 바로 보기

**▶ [웹 요약 페이지 열기](https://o-fireheart-o.github.io/Reality_Capture_Research/)**

여섯 편의 문서를 한 장으로 묶은 페이지입니다. 그림 8개, 용어 검색, 다크 모드를 지원합니다.

## 문서

| 문서 | 다루는 질문 |
|------|-------------|
| [00. 용어집](docs/00-glossary.md) | 공통 용어 69개 |
| [01. 도구 지형도](docs/01-tools.md) | 세상에는 어떤 Reality Capture 도구들이 있는가 |
| └ [COLMAP 심층](docs/01-tools/colmap.md) | 오픈소스 SfM·MVS 기준 구현은 무엇이고 어디까지 쓸 수 있는가 |
| [02. 역사와 진행 방향](docs/02-history.md) | Reality Capture는 어떤 역사를 가지고 있으며 현재 어떻게 발전해 가고 있는가 |
| [03. 현재의 쓰임새](docs/03-use-cases.md) | Reality Capture는 현 시대에 어떻게 사용되고 있는가 |
| [04. 연계 기술 지도](docs/04-adjacent-tech.md) | Reality Capture 기술과 연계할 수 있는 기술은 어떤 것이 있는가 |
| [05. 학습 로드맵](docs/05-learning-roadmap.md) | 한 가지 기술만으로는 발전하기 어려운 시대에, 무엇을 더 배워야 발전할 수 있는가 |

읽는 순서는 파일 번호를 따르면 됩니다. 역사(02)를 먼저 읽으면 도구 목록을 분류하는 어휘가 생깁니다.

## 출처 원칙

- 사실 주장에는 출처 URL을 붙였고, 확인 날짜는 2026-09-21입니다. 웹에서 얻은 사실은 빨리 낡으므로 날짜를 함께 보십시오.
- 출처 없이 쓴 판단에는 "(추정)"을 표시했습니다.
- 벤더 발표 수치와 제3자·학술 검증을 구분했습니다.

## 저장소 구조

```
docs/      리서치 원문 (마크다운 6편)
site/      웹 요약 페이지 조각과 합본(index.html)
tools/     용어집 섹션 생성 스크립트
```

웹 페이지는 `site/_0*.html` 조각을 이어 붙여 만들고, `master`에 push하면 GitHub Actions가 Pages로 배포합니다.
페이지와 원문이 다르면 원문(`docs/`)이 기준입니다.
