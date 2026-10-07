# 00. 용어집

작성일: 2026-09-21
최종수정일: 2026-10-07

Reality Capture 문서 묶음에서 쓰는 용어를 한곳에 모았다. 각 용어는 여기서 한 번만 정의하고,
다른 문서에서는 이 문서로 링크한다. 정의 뒤의 URL은 그 정의의 근거이며 확인 날짜는 2026-09-21이다.

출처를 확인하지 못한 항목은 **(추정)**으로 표시했다. 확정 전까지는 그대로 인용하지 않는 편이 안전하다.

> 수집 범위: 여섯 문서(`01`~`05` 및 이 문서)의 용어 후보를 모두 병합했다. 중복 정의는 하나로 합치고,
> 같은 용어에 출처가 여럿이면 원 논문이나 표준 원문을 우선 인용했다.

---

## 1. 총론

**Reality Capture**
실재하는 공간이나 물체를 측정해 3차원 디지털 표현으로 바꾸는 기술 전반. 특정 장비나 방식이 아니라
취득·처리·활용을 잇는 파이프라인 전체를 가리킨다. → 범위 정의는 [01-tools.md](01-tools.md) 0절

**점군(Point Cloud)**
3차원 좌표를 가진 점들의 집합으로 공간을 표현한 데이터. Reality Capture의 가장 기본적인 산출물이다.
https://www.mdpi.com/2072-4292/16/17/3256

**디지털 트윈(Digital Twin)**
물리적 자산을 디지털로 복제해 상태 변화를 지속적으로 반영하는 모델. Reality Capture는 트윈을
실측으로 갱신하는 입력 수단에 해당한다. → [04-adjacent-tech.md](04-adjacent-tech.md)

---

## 2. 취득 방식

**사진측량(Photogrammetry)**
서로 다른 각도에서 찍은 사진 여러 장에서 3차원 기하를 역산하는 측량 기법.
https://colmap.github.io/

**라이다(LiDAR)**
레이저 펄스의 왕복 시간이나 위상차로 거리를 측정해 3차원 점군을 만드는 센서.
https://toddneff.com/books/lidarhistory/extras/lidarhistory-timeline/

**TLS(Terrestrial Laser Scanning, 지상 레이저 스캐닝)**
삼각대에 고정한 스캐너가 제자리에서 회전하며 취득하는 지상 라이다. 정밀도가 높은 대신 이동마다
거치와 정합이 필요하다.
https://leica-geosystems.com/-/media/files/leicageosystems/products/datasheets/leica-rtc360-ds.ashx

**SLAM(Simultaneous Localization and Mapping)**
센서 자신의 위치와 주변 지도를 동시에 추정하는 기법. 모바일·핸드헬드 스캐너가 걸어 다니며
취득할 수 있게 하는 핵심 기술이다.
https://knowledge.navvis.com/docs/navvis-vlx-3-specifications

**ToF(Time-of-Flight)**
빛이 대상에 갔다 돌아오는 시간을 재어 거리를 구하는 방식.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8593014/

**구조광(Structured Light)**
알려진 패턴을 대상에 투사하고 그 패턴이 일그러진 모양을 관측해 형상을 계산하는 방식.
https://www.artec3d.com/portable-3d-scanners/artec-leo

**MMS(Mobile Mapping System, 이동형측량시스템)**
차량에 라이다·카메라·GNSS/INS를 싣고 주행하며 도로를 3차원으로 측량하는 시스템.
https://www.koit.co.kr/news/articleView.html?idxno=84833

**포켓 라이다**
스마트폰이나 태블릿에 내장된 소형 라이다 센서. 미국 FHWA가 굴착 트렌치 계측에 시험 적용했다.
https://highways.dot.gov/sites/fhwa.dot.gov/files/FHWA-HRT-25-015.pdf

---

## 3. 처리와 알고리즘

**SfM(Structure-from-Motion)**
영상 집합에서 카메라 자세와 희소 3차원 구조를 동시에 복원하는 절차.
https://colmap.github.io/

**MVS(Multi-View Stereo)**
자세가 이미 알려진 다시점 영상에서 조밀한 점군이나 메시를 생성하는 후속 단계.
https://colmap.github.io/

**전역 SfM(Global SfM)**
모든 사진 쌍의 상대 자세를 한꺼번에 풀어 전체 카메라 자세를 정한 뒤 번들조정을 하는 방식. 사진을 한 장씩
붙여 나가는 증분 SfM보다 빠르다. → [01-tools/colmap.md](01-tools/colmap.md) 2.3절
https://arxiv.org/abs/2407.20219

**COLMAP**
사진 묶음에서 카메라 자세와 희소 점군(SfM), 조밀 점군과 메시(MVS)를 복원하는 BSD 라이선스 오픈소스
파이프라인. 3DGS·NeRF 연구 코드가 입력 포맷으로 널리 쓴다. → [01-tools/colmap.md](01-tools/colmap.md)
https://colmap.github.io/

**번들조정(Bundle Adjustment)**
여러 시점의 관측을 한꺼번에 써서 카메라 자세와 3차원 점 좌표를 비선형 최소제곱으로 함께 보정하는 절차.
사진측량과 SLAM 양쪽의 정확도를 떠받치는 계산이다.
https://github.com/ceres-solver/ceres-solver

**정합(Registration, 점군 정합)**
서로 다른 지점에서 취득한 점군을 하나의 좌표계로 겹쳐 맞추는 작업.
https://pmc.ncbi.nlm.nih.gov/articles/PMC11207371/

**ICP(Iterative Closest Point)**
가장 가까운 점 대응을 반복해 갱신하며 두 점군 사이의 강체변환을 추정하는 고전 정합 알고리즘.
https://www.open3d.org/

**표류(Drift)**
SLAM이 추정한 궤적이 시간이 갈수록 실제 경로에서 벗어나는 누적 오차.
https://isprs-archives.copernicus.org/articles/XLVIII-1-W1-2023/517/2023/

**폐합(Loop Closure, 루프 클로저)**
이미 지나온 장소로 되돌아왔음을 인식해 누적된 표류를 보정하는 SLAM 절차.
https://isprs-archives.copernicus.org/articles/XLVIII-1-W1-2023/517/2023/

**오차상태 칼만필터(Error-State Kalman Filter)**
상태 자체가 아니라 상태의 오차를 추정해 회전의 비선형성을 다루는 필터. IMU 융합에 널리 쓰인다.
https://arxiv.org/abs/1711.02508

**팩터그래프(Factor Graph)**
변수와 제약을 이분 그래프로 표현해 SLAM과 센서 융합 문제를 푸는 방식.
https://gtsam.org/

**순전파 3D 복원(Feed-forward 3D Reconstruction)**
반복 최적화 없이 신경망 한 번의 추론으로 카메라 자세와 점군을 예측하는 방식. 전통적 SfM 파이프라인을
대체하려는 최근 흐름이다.
https://arxiv.org/pdf/2507.08448

**의미분할(Semantic Segmentation)**
점 하나하나에 벽·바닥·배관 같은 범주 이름을 붙이는 작업.
https://arxiv.org/abs/1911.11236

**RandLA-Net**
랜덤 샘플링을 써서 한 번에 100만 점 규모를 처리하는 대규모 점군 의미분할 신경망.
https://arxiv.org/abs/1911.11236

---

## 4. 신경 렌더링

**NeRF(Neural Radiance Fields)**
장면을 신경망 기반의 연속 체적 함수로 표현해 새로운 시점의 영상을 합성하는 기법. 2020년 발표.
https://arxiv.org/abs/2003.08934 (원 논문) · https://dl.acm.org/doi/abs/10.1007/978-3-030-58452-8_24

**3DGS(3D Gaussian Splatting)**
장면을 수백만 개의 3차원 가우시안으로 명시적으로 표현해 실시간 렌더링을 달성한 방사휘도장 기법. 2023년 발표.
https://arxiv.org/abs/2308.04079 (원 논문) · https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/

**신규 시점 합성(Novel View Synthesis)**
촬영하지 않은 시점에서 본 장면의 영상을 생성하는 작업. NeRF와 3DGS가 겨루는 공통 과제다.
https://arxiv.org/abs/2003.08934

**3D VLM(3D Vision-Language Model)**
3차원 임베딩을 이미지·텍스트와 정렬해 자연어로 3차원 데이터를 질의할 수 있게 하는 모델.
https://arxiv.org/abs/2609.05583

**Set-of-Mark 프롬프팅**
이미지의 관심 영역에 표시를 얹어 멀티모달 LLM의 분석 정확도를 높이는 기법.
http://www.iaarc.org/publications/2024_proceedings_of_the_41st_isarc_lille_france/automated_inspection_report_generation_using_multimodal_large_language_models_and_set-of-mark_prompting.html

---

## 5. 데이터 포맷과 표준

**E57(ASTM E2807)**
점 좌표·색·강도와 2차원 영상을 함께 담는 벤더 중립 점군 교환 포맷. 2011년 2월 ASTM 승인.
https://www.ri.cmu.edu/pub_files/2011/1/2011-huber-e57-v3.pdf · https://paulbourke.net/dataformats/e57/

**LAS / LAZ**
ASPRS가 정한 라이다 점군 바이너리 표준 포맷과 그 무손실 압축본.
https://www.loc.gov/preservation/digital/formats/fdd/fdd000418.shtml

**COPC(Cloud Optimized Point Cloud)**
단일 파일 안에서 옥트리로 공간 정렬해 HTTP 부분 읽기를 가능하게 만든 점군 포맷.
https://lidarnews.com/cloud-optimized-point-clouds-copc/

**3D Tiles**
대용량 3차원 지리공간 데이터를 계층 타일로 나눠 스트리밍하는 OGC 표준.
https://www.ogc.org/standards/3dtiles/

**I3S(Indexed 3D Scene Layers)**
대용량 3차원 콘텐츠의 스트리밍과 저장을 위한 OGC 커뮤니티 표준.
https://www.ogc.org/announcement/new-version-of-3d-streaming-community-standard-i3s-adopted-and-published-by-ogc/

**옥트리 LOD(Octree Level of Detail)**
공간을 8분할로 재귀 분할해 보는 거리에 따라 다른 해상도를 내보내는 자료구조.
https://github.com/potree/potree

**Potree**
TU Wien에서 나온 무료 오픈소스 WebGL 점군 뷰어.
https://github.com/potree/potree

**OpenUSD**
여러 도구 사이에서 대규모 3차원 장면을 조립하고 교환하기 위한 개방 규격.
https://aousd.org/news/alliance-for-openusd-announces-new-member-milestone-industrial-momentum-and-core-specification-progress/

---

## 6. BIM과 건설

**IFC(Industry Foundation Classes)**
buildingSMART의 벤더 중립 개방형 BIM 데이터 스키마. IFC4.3이 ISO 16739-1:2024로 발행되었다.
https://www.iso.org/standard/84123.html

**Scan-to-BIM**
취득한 점군에서 바닥·벽·개구부 같은 건축 객체를 인식해 의미를 가진 BIM 모델로 변환하는 작업.
https://www.opendesign.com/products/scan-to-bim

**scan-vs-BIM**
스캔 점군을 기존 BIM 모델과 대조해 설치 여부와 시공 오차를 판정하는 작업. 모델을 새로 만드는
Scan-to-BIM과 목적이 다르다.
https://cintoo.com/en/blog/progress-monitoring

**as-built BIM**
설계 모델이 아니라 실제 시공된 상태를 반영한 BIM 모델.
https://doi.org/10.1016/j.autcon.2025.106755

**COBie**
준공 시점에 장비 목록·보증·예방정비 정보를 발주처에 넘기기 위한 자산 정보 규격.
https://en.wikipedia.org/wiki/COBie

**ISO 19650**
건설 자산 생애주기 전반의 정보관리를 다루는 국제표준 시리즈.
https://www.iso.org/standard/68078.html

**IfcMapConversion**
모델의 로컬 좌표를 지도 좌표로 옮기는 변환을 담는 IFC 엔티티.
https://isprs-annals.copernicus.org/articles/X-4-W2-2022/145/2022/

**IfcProjectedCRS**
모델이 사용하는 투영 좌표계를 EPSG 코드 등으로 명시하는 IFC 엔티티.
https://isprs-annals.copernicus.org/articles/X-4-W2-2022/145/2022/

---

## 7. 좌표계와 정확도

**GCP(Ground Control Point, 지상기준점)**
좌표를 이미 아는 지상 표적으로, 취득 결과를 절대 좌표에 고정하는 기준이 된다.
https://enterprise.dji.com/zenmuse-l2/specs

**GSD(Ground Sample Distance)**
영상 한 픽셀이 대응하는 지상 거리. 촬영 계획과 기대 정확도를 잇는 값이다.
https://www.ipb.uni-bonn.de/photogrammetry-i-ii/

**KGD2002(한국측지계 2002)**
GRS80 타원체와 ITRF2000 데이텀에 기반한 대한민국 세계측지계 성과.
https://www.ngii.go.kr/other/file_down.do?sq=101741

**LOA(Level of Accuracy)**
USIBD가 정의한 기존 시설물 문서화 정확도 등급. LOA 10부터 LOA 50까지 나뉜다.
http://usibd.org/product/usibd-level-of-accuracy-loa-specification-guide-version-3-0-2019/

**QL(Quality Level, 품질 등급)**
USGS 3DEP이 정한 라이다 점밀도와 수직정확도 등급 체계.
https://www.usgs.gov/3d-elevation-program/topographic-data-quality-levels-qls

**헬머트 7 파라미터 변환**
원점 이동 3개, 축척 1개, 회전 3개로 두 좌표계를 잇는 상사 변환. **(추정 — 출처 미확인)**

---

## 8. 연계 기술

**공간 앵커(Spatial Anchor)**
가상 객체에 현실 세계의 위치와 방향을 부여하는 월드 고정 기준계. AR 현장 중첩의 토대다.
https://developers.meta.com/horizon/documentation/unity/unity-spatial-anchors-overview/

**GrandSLAM**
LiDAR SLAM·비주얼 SLAM·IMU를 묶은 Leica BLK ARC의 자율 주행·캡처 기술.
https://leica-geosystems.com/products/laser-scanners/scanners/leica-blk-arc

**Autowalk**
Boston Dynamics Spot이 미리 지정한 경로를 사람 개입 없이 반복 주행하는 기능.
https://leica-geosystems.com/about-us/news-room/news-overview/2024/09/leica-blk-arc-now-the-first-certified-reality-capture-device-available-for-boston-dynamics-spot

**도메인 갭(Domain Gap)**
학습 데이터와 실제 데이터의 분포 차이 때문에 성능이 떨어지는 현상. 합성 점군으로 학습할 때
가장 자주 부딪히는 장애다.
https://www.sciencedirect.com/science/article/abs/pii/S0926580524002097

---

## 9. 역사 용어

기술사 서술에 등장하는 옛 장비와 명칭이다. → [02-history.md](02-history.md)

**métrophotographie(계측사진법)**
에메 로쉐다가 자신의 사진 기반 지형 측량 기법에 붙인 최초의 명칭.
https://onlinelibrary.wiley.com/doi/10.1111/phor.12277

**도화기(Stereoplotter)**
중첩 촬영한 두 장의 사진을 입체로 관측해 지형과 구조물을 도면화하는 장비.
https://www.asprs.org/wp-content/uploads/pers/1969journal/nov/1969_nov_1160-1168.pdf

**해석적 도화기(Analytical Plotter)**
기계적 링키지 대신 컴퓨터 연산으로 사진의 기하 관계를 푸는 도화기.
https://www.semanticscholar.org/paper/New-principle-for-photogrammetric-plotters-Helava/035a49800133648d2fdf5a3ed03edd1101862ea9

**디지털 사진측량 워크스테이션(DPW, Softcopy Photogrammetry)**
필름 대신 디지털 화소 영상을 다뤄 대응점 탐색을 자동화한 사진측량 시스템.
https://www.sciencedirect.com/science/article/pii/S1195103624002556

---

## 10. 현장·실무 용어

실제 취득과 운영에서 쓰는 말이다. → [03-use-cases.md](03-use-cases.md)

**차폐(Occlusion)**
다른 물체에 가려 스캐너 시야에 들어오지 않아 점군에 구멍이 생기는 현상. 현장 취득 품질을
떨어뜨리는 가장 흔한 원인이다.
https://doi.org/10.1016/j.autcon.2025.106755

**커버리지 비율**
특정 부재를 스캔 데이터가 얼마나 덮었는지 나타내는 지표. 이 값이 낮으면 편차 판정을 신뢰할 수 없다.
https://cintoo.com/en/blog/progress-monitoring

**event walk**
마감재에 덮이기 전 상태를 기록으로 남기려고 특정 시점에 현장을 도는 360 촬영.
https://www.openspace.ai/resources/case-studies/devcon-construction-uses-openspace-to-capture-a-complete-record-of-1-6m-square-foot-project-site/

**First Time Right**
스캔 기반 간섭 검토로 사전 제작한 배관 스풀이 현장에서 한 번에 맞도록 하는 목표.
https://www.asbuilt3d.com/post/pre-turnaround-laser-scanning-checklist

**정사영상(Orthomosaic)**
항공·드론 사진의 기하 왜곡을 보정해 지도처럼 축척이 일정하도록 이어 붙인 영상.
https://dronelife.com/2019/01/08/california-drones-stitch-helpful-aerial-maps-in-wake-of-deadly-camp-fire/

**LED 볼륨**
실사 배경을 띄운 LED 월로 둘러싼 촬영 세트. 취득한 에셋을 Unreal Engine으로 띄워 쓴다.
https://www.kiriengine.app/blog/3DGSvsPhotogrammetryvsLiDAR

---

## 11. 지도와 아카이브

**정밀도로지도**
자율주행 지원을 위해 차선·도로시설·표지시설을 3차원으로 제작한 전자지도. 국토지리정보원이 구축하고 갱신한다.
https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000229524

**HD맵**
차선 단위 형상과 도로 경계, 교통 통제 요소를 센티미터급 정확도로 담은 자율주행용 지도.
https://www.marketsandmarkets.com/Market-Reports/hd-map-autonomous-vehicle-market-141078517.html

**Open Heritage**
CyArk와 Google Arts & Culture가 공개한 문화유산 3차원 데이터 아카이브.
https://artsandculture.google.com/story/open-heritage-sharing-3d-data-with-the-world/-AXx62Vr4vwlKA
