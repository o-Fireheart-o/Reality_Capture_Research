# 05. 학습 로드맵 — 무엇을 더 배워야 발전할 수 있는가

작성일: 2026-09-21
최종수정일: 2026-10-07

> **담당 질문(핵심 연구 질문 5)**: 한 가지 기술만으로는 발전하기 어려운 시대에, 무엇을 더 배워야 발전할 수 있는가
>
> **범위 렌즈**: 전 산업을 훑되 건설·AEC 관점을 주 렌즈로 삼는다. 자율주행·문화재·플랜트 사례도 참고하지만, 우선순위를 매길 때의 기준은 "건설 현장과 BIM 워크플로에서 값이 나오는가"다.

## 0. 이 문서를 읽는 법

- 여기 적힌 학습 자원은 2026-09-21에 하나씩 확인한 것만 실었다. 존재를 확인하지 못한 자료는 넣지 않았다.
- URL 뒤의 `†` 표시는 그 사이트가 자동 조회를 막거나(403, 인증서 오류, 리다이렉트 루프) 본문을 읽어 오지 못해, 검색 결과에 인용된 내용과 표준 번호로만 교차 확인했다는 뜻이다. 문서가 있다는 사실은 확인했지만 본문은 읽지 못했다.
- 본문 안에 `[제목](URL)` 형태로 넣은 학술 출판사(Springer, ScienceDirect) 링크와 채용 사이트 링크, 시장조사 보고서 링크도 같은 사정이다. 서지정보와 초록 수준까지만 확인했고 전문은 읽지 못했다. 표시가 지저분해져 `†`를 따로 붙이지 않았으니 이 문단을 기준으로 읽으면 된다.
- 출처가 없는 판단에는 `(추정)`을 붙였다. 특히 학습 기간 숫자는 전부 추정이다. 사람마다 배경이 다르므로 그대로 믿지 말고 자기 출발점에 맞춰 늘리거나 줄이면 된다.
- 벤더가 만든 자료와 학술·제3자 자료를 구분해 표기했다.

---

## 1. 전제: 왜 기술 하나로는 부족한가

막연한 자기계발 구호 대신 이 분야에서 실제로 관찰되는 사실 세 가지에서 출발한다.

### 1.1 채용이 요구하는 능력의 폭이 이미 넓다

Reality Capture 직무 공고를 읽어 보면 장비 운용 하나만 요구하는 자리는 드물다. Amazon의 Reality Capture BIM Engineer 공고는 Autodesk 계열(Civil 3D, Revit, Navisworks, ReCap, BIM 360) 경험과 점군 처리·모델링 경험을 함께 요구한다([amazon.jobs 공고 2503498](https://www.amazon.jobs/en/jobs/2503498/reality-capture-bim-engineer), 확인 2026-09-21 — 채용 공고이므로 1차 자료). Los Alamos National Laboratory의 Reality Capture Specialist 공고는 현장 스캐닝, 점군 정합과 품질관리, scan-to-BIM을 한 사람이 독립적으로 수행해야 한다고 명시한다([lanl.jobs](https://lanl.jobs/search/jobdetails/reality-capture-specialist-lidar-registration-and-bim-modeling/e9dcedcb-c944-4c60-b67c-4bf854943fbf), 확인 2026-09-21).

이런 공고에서 반복되는 항목이 하나 있다. 좌표계와 단위, 측량 기준점을 이해하고 있느냐다. 장비를 잘 다루는 사람이 아니라 측량 기준계와 BIM 좌표계 사이에서 데이터를 잃지 않고 옮길 줄 아는 사람을 찾는다.

### 1.2 "자동화되니까 안 배워도 된다"는 아직 사실이 아니다

scan-to-BIM 자동화 연구는 오래 쌓였지만 리뷰 계열 연구가 내놓는 결론은 여전히 비슷하다. 딥러닝 기반 분할이 벽·바닥·천장 같은 주요 부재까지는 처리해도 나머지 객체는 사람이 모델링해야 하고, 가려진(occluded) 영역은 복원이 어렵다. 학습에 필요한 라벨링 점군을 구하는 비용도 병목이다. 합성 데이터로 메우려 하면 도메인 갭 탓에 정확도가 떨어진다([Harnessing Indoor 3D Point Cloud Reconstruction for Automated Scan-to-BIM Workflows: A Systematic Review, Springer](https://link.springer.com/chapter/10.1007/978-981-92-2743-3_40), 확인 2026-09-21 — 학술 리뷰; [DawNet, Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S0926580524002097), 확인 2026-09-21 — 학술 논문).

당분간 값이 붙는 자리는 자동화 결과를 판단하고 고치는 사람 쪽이다. 판단하려면 원리를 알아야 한다.

### 1.3 신기술의 정확도 한계가 곧 학습 항목이 된다

3D Gaussian Splatting은 2023년 논문 발표 이후 급속히 퍼졌다([graphdeco-inria/gaussian-splatting, ACM TOG 42(4), 2023](https://github.com/graphdeco-inria/gaussian-splatting), 확인 2026-09-21 — 저자 공개 구현). 그런데 건물을 대상으로 공간 정확도를 측정한 ISPRS 연구를 보면 3DGS의 정확도는 입력 영상 수와 초기 점군 품질, 학습 반복 횟수 같은 조건에 크게 좌우된다. 같은 연구에서 영상 기반 초기화(COLMAP, Pix4D)가 휴대폰 LiDAR 초기화보다 공간 지표에서 나았다([McNally 외, A Comprehensive Evaluation of the Spatial Accuracy of Building Gaussian Splatting, ISPRS Annals XI-M-1-2026](https://isprs-annals.copernicus.org/articles/XI-M-1-2026/31/2026/isprs-annals-XI-M-1-2026-31-2026.html), 확인 2026-09-21 — 학술 논문).

콘크리트 부재를 대상으로 3DGS와 레이저 스캐닝을 비교한 연구도 비슷하다. 전체 형상은 비슷하게 나왔지만 평면 노이즈가 커서 레이저 스캔 점군에서는 보이던 처짐과 휨 세부가 3DGS 점군에서 사라졌다([Comparing 3D Gaussian Splatting and Laser Scanning for Assessing the Condition of Structural Concrete Elements for Circular Reuse, Springer](https://link.springer.com/chapter/10.1007/978-981-95-8489-5_53), 확인 2026-09-21 — 학술 논문).

여기서 실무자가 답해야 할 질문이 생긴다. 어느 용도에 어느 센서를 쓸 것인가. 이 판단을 내리려면 기하학·측량 오차론·품질 규격을 모두 알아야 한다. 도구 사용법만 알아서는 답이 나오지 않는다.

---

## 2. 기반 역량

항목마다 "왜 필요한가", "어디까지 하면 되는가", "대표 자원"을 붙였다. 순서는 중요도가 아니라 의존 관계를 따랐다.

### 2.1 선형대수와 3D 기하 — 좌표변환, 회전 표현

**왜**: Reality Capture의 오류는 결국 좌표계 문제로 환원된다. 스캔 월드 좌표, 프로젝트 좌표, 측량 기준계, BIM 내부 좌표 사이에는 저마다 다른 변환 관계가 있다. 회전을 오일러각으로 다루다 짐벌락을 만나거나, 스케일이 섞인 유사변환을 강체변환으로 착각하는 사고가 현장에서 반복된다.

**어디까지**: 동차좌표, SE(3)/SO(3), 쿼터니언과 회전행렬의 상호 변환, 유사변환(7-parameter Helmert)과 강체변환의 차이, 최소제곱 기반 점군 정렬(Kabsch/Horn)을 손으로 유도할 수 있으면 충분하다.

**대표 자원**

- Joan Solà, *Quaternion kinematics for the error-state Kalman filter* — 쿼터니언, 회전군의 Lie 구조, 회전 섭동과 미분을 실전 추정식까지 끌고 간다 — https://arxiv.org/abs/1711.02508 (확인 2026-09-21, 학술 자료·무료)
- Cyrill Stachniss, *Photogrammetry I & II* 중 동차좌표·카메라 외부/내부표정 강의 — https://www.ipb.uni-bonn.de/photogrammetry-i-ii/ (확인 2026-09-21, 대학 강의·영상 무료)

### 2.2 사진측량 원리

**왜**: SfM 소프트웨어의 버튼은 몇 개 안 되지만 결과가 틀렸을 때 원인을 찾으려면 그 안에서 무슨 일이 일어나는지 알아야 한다. 촬영 계획(중복도, 촬영 고도, GSD), 표정 요소, 지상기준점(GCP) 배치, 렌즈 왜곡 모델을 모르면 "왜 휘었는지" 설명하지 못한다.

**어디까지**: 내부표정과 외부표정의 구분, 공선조건식, 전방교회법, 항공삼각측량, 정사영상 생성 원리. 여기에 더해 GSD와 기대 정확도의 관계를 계산할 줄 알아야 한다.

**대표 자원**

- Cyrill Stachniss, *Photogrammetry I & II* (Uni Bonn) — 카메라 기초부터 에피폴라 기하, 번들조정, 항공삼각측량, 정사영상까지 학부 두 학기 분량. 영상은 공개, 슬라이드는 강의자 이메일 요청 — 강의 페이지 https://www.ipb.uni-bonn.de/photogrammetry-i-ii/ , 2021년 플레이리스트 https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y † (확인 2026-09-21, 대학 강의·무료)
- Richard Hartley, Andrew Zisserman, *Multiple View Geometry in Computer Vision*, 2nd ed., Cambridge University Press, 2004 — 다시점 기하의 정본. 에피폴라 기하와 삼중초점 텐서 등 일부 장은 무료 PDF — https://www.robots.ox.ac.uk/~vgg/hzbook/ (확인 2026-09-21, 학술 교재·일부 무료)

### 2.3 확률과 최적화 — 번들조정, 상태추정

**왜**: 번들조정은 Reality Capture 파이프라인의 심장이다. 어느 관측을 얼마나 믿을지(가중치), 이상치를 어떻게 걷어낼지(robust loss), 해가 왜 발산하는지를 이해하지 못하면 정합 실패 앞에서 재촬영밖에 할 게 없다. 모바일 매핑과 SLAM으로 넘어가면 칼만 필터 계열과 팩터그래프가 바로 뒤따른다.

**어디까지**: 비선형 최소제곱(Gauss-Newton, Levenberg-Marquardt), 희소 야코비안 구조, 공분산 전파, 로버스트 손실함수, EKF와 그래프 기반 SLAM의 차이.

**대표 자원**

- Timothy D. Barfoot, *State Estimation for Robotics*, 2nd ed., Cambridge University Press, 2024(초판 2017) — 저자 페이지에서 PDF를 무료 공개한다. 행렬 Lie군 위의 추정을 한 권으로 정리했다 — http://asrl.utias.utoronto.ca/~tdb/ (확인 2026-09-21, 학술 교재·무료)
- Ceres Solver — Google이 2010년부터 유지하는 비선형 최소제곱 라이브러리. 번들조정 예제가 문서에 포함돼 있다 — https://github.com/ceres-solver/ceres-solver (확인 2026-09-21, 오픈소스)
- GTSAM — 팩터그래프 기반 센서융합 라이브러리. BSD 라이선스, C++에 Python·MATLAB 바인딩 — https://gtsam.org/ (확인 2026-09-21, 오픈소스)

### 2.4 컴퓨터 비전 기초

**왜**: 특징점 검출과 매칭, 스테레오 정합, 삼각측량은 사진측량과 컴퓨터 비전이 같은 문제를 다른 어휘로 부르는 영역이다. 두 어휘를 모두 알아야 논문과 벤더 문서를 오갈 수 있다. 딥러닝 기반 매칭이 고전 기법을 대체해 가는 흐름을 읽으려면 더더욱 그렇다.

**어디까지**: 필터링·에지·특징기술자, RANSAC, 기본행렬과 필수행렬, 스테레오와 MVS, 최근의 학습 기반 매칭.

**대표 자원**

- Richard Szeliski, *Computer Vision: Algorithms and Applications*, 2nd ed., 2022 — 전자판을 저자 사이트에서 개인 사용 목적으로 내려받을 수 있다(재배포 금지) — https://szeliski.org/Book/ (확인 2026-09-21, 학술 교재)

### 2.5 점군 처리

**왜**: 촬영이 끝나면 일이 시작된다. 정합, 노이즈 제거, 다운샘플링, 분할, 메시화, 포맷 변환이 실무 시간의 대부분을 먹는다. 라이브러리 서너 개는 코드로 다룰 줄 알아야 한다.

**어디까지**: ICP 계열 정합(point-to-point, point-to-plane, colored ICP)과 전역 정합의 차이, 복셀 다운샘플링, 법선 추정, RANSAC 평면 분할, 포맷(E57/LAS/LAZ/PLY) 상호 변환.

**대표 자원**

- Open3D — MIT 라이선스, C++/Python, 정합·재구성·시각화·ML 연동을 한 패키지로 제공한다 — https://www.open3d.org/ , 저장소 https://github.com/isl-org/Open3D (확인 2026-09-21, 오픈소스)
- Point Cloud Library(PCL) — BSD 라이선스 C++ 라이브러리. 필터, 특징, 정합, 분할, 표면 재구성 모듈로 나뉜다 — https://pointclouds.org/ (확인 2026-09-21, 오픈소스)
- PDAL(Point Data Abstraction Library) — "점군의 GDAL". JSON 파이프라인으로 30여 개 포맷 변환과 좌표계 변환, 필터링을 선언적으로 기술한다 — https://pdal.org/ (확인 2026-09-21, 오픈소스)
- CloudCompare — 점군·메시 비교와 거리 계산에 쓰는 오픈소스 데스크톱 도구. 실무 검수에서 사실상 표준처럼 쓰인다(추정) — https://www.cloudcompare.org/ (확인 2026-09-21, 오픈소스)

### 2.6 프로그래밍 — Python과 C++

**왜**: Python 없이는 실험 속도가 나지 않고, C++ 없이는 성능이 필요한 지점에서 막힌다. 이 분야의 핵심 라이브러리가 C++로 짜여 Python 바인딩을 얹는 구조라 두 언어를 오가는 일이 잦다. COLMAP은 PyCOLMAP을, Open3D와 GTSAM은 각자 Python 바인딩을 제공한다.

**어디까지**: Python은 NumPy 벡터화, 시각화, 데이터 파이프라인 작성까지. C++는 남의 코드를 읽고 빌드하고 고치는 수준이면 시작으로 충분하다. CMake로 의존성을 엮어 빌드할 줄 아는 게 실질적인 진입 장벽이다.

**대표 자원**

- COLMAP 문서 — SfM/MVS 파이프라인의 CLI와 PyCOLMAP 바인딩, 입출력 포맷 설명 — https://colmap.github.io/ (확인 2026-09-21, 오픈소스 문서)

### 2.7 클라우드와 데이터 엔지니어링

**왜**: 현장 하나에서 수십 GB, 프로젝트 하나에서 테라바이트가 나온다. 로컬 워크스테이션으로 버티는 단계를 넘어서면 저장·전송·스트리밍이 곧 제품 경쟁력이 된다. 플랫폼형 사업에서는 이 영역이 본체다.

**어디까지**: 옥트리 기반 LOD 구조, 클라우드 네이티브 포맷(COPC, EPT), HTTP range request 기반 부분 로딩, 객체 스토리지 비용 구조, 배치 처리 오케스트레이션.

**대표 자원**

- Potree — WebGL 점군 렌더러. 옥트리 다중해상도 구조로 대용량 점군을 브라우저에 띄운다. TU Wien 연구에서 출발했다 — https://github.com/potree/potree (확인 2026-09-21, 오픈소스)
- PDAL 파이프라인 문서 — 대량 점군 배치 처리와 좌표변환을 선언적으로 기술하는 방식 — https://pdal.org/ (확인 2026-09-21, 오픈소스 문서)
- Cloud Optimized Point Cloud(COPC) 해설 — 단일 파일 안에 옥트리로 공간 정렬해 부분 읽기를 가능하게 하는 포맷 — https://lidarnews.com/cloud-optimized-point-clouds-copc/ † (확인 2026-09-21, 업계 매체)

---

## 3. 도메인 지식

기술만 익히고 도메인을 건너뛰면 정확한데 쓸모없는 산출물이 나온다.

### 3.1 건설 공정과 BIM 워크플로

발주-설계-시공-유지관리 단계마다 필요한 정보가 다르다. 스캔 데이터가 어느 단계의 어떤 의사결정에 들어가는지 모르면 납품 규격을 정할 수 없다.

- **ISO 19650 시리즈** — 건설 자산의 생애주기 정보관리 국제표준. Part 1은 개념과 원칙, Part 2는 자산 인도 단계의 정보관리 프로세스를 규정한다 — https://www.iso.org/standard/68078.html † (확인 2026-09-21, 국제표준)
- **IFC / ISO 16739-1:2024** — openBIM 데이터 교환 스키마. IFC4.3이 2024년 3월 ISO 표준으로 발행됐고, 인프라 영역까지 확장됐다 — https://www.iso.org/standard/84123.html † (확인 2026-09-21, 국제표준)
- **IfcOpenShell** — IFC를 코드로 읽고 쓰는 오픈소스 툴킷. IFC2X3/IFC4/IFC4X3을 지원하며 C++과 Python에서 쓸 수 있다 — https://ifcopenshell.org/ (확인 2026-09-21, 오픈소스)
- **국토교통부 「건설산업 BIM 기본지침」** — 2020년 12월 발표. BIM 정의, 적용 대상, 절차, 공통 표준을 제시한다 — https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4516 † , 보도자료 https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95084979 † (확인 2026-09-21, 정부 지침)
- **국토교통부 「건설산업 BIM 시행지침」** — 발주자편·설계자편·시공자편으로 나뉜 실행 지침 — https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4634 † (확인 2026-09-21, 정부 지침)

### 3.2 측량 기준계

국내 현장에서 일한다면 피할 수 없다. 한국은 2002년 1월 1일부터 동경측지계를 버리고 세계측지계 기반의 한국측지계 2002(KGD2002)를 쓴다. GRS80 타원체에 ITRF2000 데이텀을 쓰고, 국가기본도 평면직각좌표계는 경도 2도 간격 네 개 원점 체계다. 표고 기준은 인천만 평균해면이다.

- 국토지리정보원 「세계측지계 기술지침서」(2004) — https://www.ngii.go.kr/other/file_down.do?sq=101741 † (확인 2026-09-21, 정부기관 발행)
- 대한민국 EPSG 코드 정리 — 실무에서 좌표계 코드를 고를 때 참고할 만한 정리 — http://www.gisdeveloper.co.kr/?p=8942 † (확인 2026-09-21, 개인 기술 블로그·2차 자료)

기준계를 배우는 목적은 암기가 아니다. 스캔 좌표를 국가 좌표계에 물릴 때 어떤 변환이 어떤 오차를 낳는지 예측하는 데 있다.

### 3.3 데이터 표준과 품질 규격

- **E57 / ASTM E2807** — 벤더 중립 점군 교환 포맷. 2011년 2월 ASTM 표준으로 승인됐고, XML 메타데이터와 바이너리 점 데이터를 결합한 구조다. 점 좌표·색·강도와 2D 영상을 함께 담는다 — https://paulbourke.net/dataformats/e57/ (확인 2026-09-21, 대학 소속 기술 문서), 라이브러리 http://libe57.org/ † (확인 2026-09-21, 오픈소스)
- **ASPRS LAS 1.4(R15)** — 항공 LiDAR 표준 포맷. 분류 필드 256종 확장, WKT 좌표계 표기, 다중 센서 지원이 주요 변경점이다 — 사양서 PDF https://paulbourke.net/dataformats/laz/LAS_1_4_r15.pdf † (확인 2026-09-21, 발행처는 ASPRS)
- **USIBD Level of Accuracy(LOA) Specification, Version 3.0(2019)** — 기존 시설물 문서화의 정확도 등급 규격. LOA 10(약 50 mm)부터 LOA 50(약 1 mm)까지 다섯 단계로 나눈다. 여기서 헷갈리기 쉬운 지점이 있다. 이 허용오차는 "실제 건물 대비 모델"이 아니라 "점군 대비 BIM 요소"에 적용된다. 점군 자체의 정확도는 별개 문제로 남는다 — http://usibd.org/product/usibd-level-of-accuracy-loa-specification-guide-version-3-0-2019/ (확인 2026-09-21, 업계 단체 규격), 요약 발표자료 https://cdn.ymaws.com/www.nysapls.org/resource/resmgr/2019_conference/handouts/hale-g_bim_loa_guide_c120_v2.pdf † (확인 2026-09-21, 업계 발표자료)

---

## 4. T자형 조합 시나리오

세로획은 Reality Capture다. 가로획을 무엇으로 그을지가 진로를 가른다. 네 가지를 제시한다. 기간은 전부 추정이며, 2장의 기반 역량을 어느 정도 갖췄다는 전제다.

### 4.1 RC + ML 엔지니어

**조합**: Reality Capture + 3D 딥러닝(분할·검출·재구성)

**푸는 실제 문제**: 점군에서 벽·기둥·보·배관을 자동으로 찾아내 모델링 시간을 줄이는 일. 1.2에서 봤듯 이 문제는 아직 풀리지 않았다. 주요 부재 너머의 객체, 가려진 영역, 라벨 데이터 부족과 도메인 갭이 남은 과제다([Springer 리뷰](https://link.springer.com/chapter/10.1007/978-981-92-2743-3_40), 확인 2026-09-21). 뒤집어 보면 아직 들어갈 자리가 남아 있다.

**필요한 학습 항목**

- 3D 딥러닝 아키텍처: 희소 컨볼루션, Point Transformer 계열
- 대규모 점군 데이터 파이프라인과 라벨링 전략
- 도메인 적응, 합성 데이터 생성
- 평가 지표: mIoU와 기하 오차를 함께 보는 습관
- 실습 코드베이스: Pointcept — PTv1/v2/v3, SparseUNet 등을 ScanNet·S3DIS·SemanticKITTI·nuScenes 설정으로 제공한다. MIT 라이선스 — https://github.com/Pointcept/Pointcept (확인 2026-09-21, 오픈소스)

**예상 진입 기간**: 파이썬과 딥러닝 경험이 있으면 6~9개월, 밑바닥부터면 12~18개월(추정)

### 4.2 RC + BIM·AEC 컨설턴트

**조합**: Reality Capture + 건설 정보관리·표준

**푸는 실제 문제**: 발주처가 "스캔 떠 주세요"라고만 말할 때, 무엇을 얼마의 정확도로 어떤 포맷으로 납품할지 정의해 주는 일. LOA 등급 선택, 좌표계 합의, IFC 교환 규칙, 검수 기준 작성이 여기 속한다. 장비를 다루는 인력은 많아도 규격을 쓸 줄 아는 사람은 드물다(추정).

**필요한 학습 항목**

- ISO 19650 정보관리 프로세스와 국토교통부 BIM 지침 체계
- USIBD LOA 등급 체계와 그 한계(점군 대비 모델 허용오차라는 점)
- IFC 스키마 구조와 MVD, 교환 요구사항 정의
- 측량 기준계와 프로젝트 좌표계 정합 절차
- 자격: buildingSMART Professional Certification — Foundation과 Practitioner 두 단계. Foundation은 국제표준 기반 5개 학습 모듈을 다루고, 객관식 25문항에서 75% 이상이면 합격이다 — https://education.buildingsmart.org/ † (확인 2026-09-21, 국제 인증기관)

**예상 진입 기간**: 건설 실무 경험이 있으면 6~12개월. 없으면 현장 경험을 쌓는 기간을 따로 잡아야 한다(추정)

### 4.3 RC + 플랫폼·클라우드 엔지니어

**조합**: Reality Capture + 대용량 공간데이터 서비스

**푸는 실제 문제**: 현장에서 올라온 수 TB 점군을 브라우저에서 즉시 돌려 보게 만드는 일. 옥트리 타일링, 부분 스트리밍, 버전 관리, 권한 관리, 비용 최적화가 전부 이 사람 몫이다. 건설 디지털 트윈 시장 자체는 성장 전망이 나오지만(예: 2025년 45억 달러에서 2026년 56억 달러 추정, [DataNext Research](https://datanextresearch.com/report/construction-digital-twin-market), 확인 2026-09-21 — 상업적 시장조사 보고서이므로 수치는 참고만 한다), 실제 서비스 품질은 이 엔지니어링에서 갈린다.

**필요한 학습 항목**

- 공간 인덱싱: 옥트리, LOD, COPC/EPT 같은 클라우드 네이티브 포맷
- 웹 3D 렌더링: WebGL/WebGPU, Potree·Cesium 계열 뷰어 구조
- 배치 처리 오케스트레이션과 객체 스토리지 비용 모델
- PDAL 기반 변환 파이프라인 자동화
- 서버 사이드 좌표계 변환

**예상 진입 기간**: 백엔드 경험이 있으면 6~12개월(추정)

### 4.4 RC + 제품기획·사업개발

**조합**: Reality Capture + 고객 문제 정의

**푸는 실제 문제**: 기술은 되는데 안 팔리는 상황을 푸는 일. 어느 공정에서 누가 무엇 때문에 돈을 쓰는지, 경쟁 대안이 사람인지 다른 소프트웨어인지, 정확도 요구가 규격에서 오는지 관행에서 오는지를 구분해야 한다. 1.3에서 인용한 3DGS 정확도 연구 같은 자료를 읽고 "이 용도에는 쓸 수 있고 저 용도에는 못 쓴다"를 판단하는 능력이 핵심 자산이 된다.

**필요한 학습 항목**

- 건설 공정과 원가 구조, 발주 방식
- 정확도 규격을 읽고 고객 요구로 번역하는 능력(LOA, ISO 19650)
- 경쟁 제품의 기술적 한계를 스스로 검증할 만큼의 기술 이해 — 최소한 4.2 수준
- 데이터 분석과 사용자 인터뷰

**예상 진입 기간**: 기술 배경이 있으면 3~6개월, 도메인 학습은 계속(추정)

> **고르는 법**: 4.1은 연구 조직이나 대형 벤더, 4.2는 엔지니어링사와 발주처, 4.3은 SaaS 기업, 4.4는 제품 조직에 자리가 있다. 지금 속한 조직에 없는 역할을 고르면 연습할 기회가 없다는 점도 함께 따져 봐야 한다(추정).

---

## 5. 단계별 로드맵

### 5.1 0~3개월 — 한 번은 끝까지 돌려 본다

목표는 이해가 아니라 완주다. 사진 몇 장에서 점군까지 스스로 만들어 보면 이후 문서를 읽을 때 얻는 것이 달라진다.

| 항목 | 무엇을 배우나 | 자원 |
|------|---------------|------|
| SfM/MVS 파이프라인 | 특징 매칭 → 카메라 자세 복원 → 밀집 재구성의 전 과정 | COLMAP 문서 https://colmap.github.io/ (확인 2026-09-21) |
| 사진측량 기초 이론 | 카메라 모델, 표정, 에피폴라 기하 | Stachniss *Photogrammetry I* 영상 https://www.youtube.com/playlist?list=PLgnQpQtFTOGRYjqjdZxTEQPZuFHQa7O7Y † (확인 2026-09-21) |
| 점군 다루기 | 로딩, 다운샘플링, 법선 추정, ICP 정합 | Open3D https://www.open3d.org/ (확인 2026-09-21) |
| 검수 감각 | 두 점군의 거리 계산, 단면 확인 | CloudCompare https://www.cloudcompare.org/ (확인 2026-09-21) |
| 좌표계 | 세계측지계, 평면직각좌표계 원점 체계 | 국토지리정보원 세계측지계 기술지침서 https://www.ngii.go.kr/other/file_down.do?sq=101741 † (확인 2026-09-21) |

### 5.2 3~12개월 — 원리로 내려가고 도메인으로 넓힌다

| 항목 | 무엇을 배우나 | 자원 |
|------|---------------|------|
| 다시점 기하 | 기본행렬·필수행렬, 삼각측량, 번들조정의 수학 | Hartley & Zisserman *MVG* 2nd ed. https://www.robots.ox.ac.uk/~vgg/hzbook/ (확인 2026-09-21) |
| 컴퓨터 비전 전반 | 특징, 스테레오, 학습 기반 방법의 위치 | Szeliski *Computer Vision* 2nd ed. https://szeliski.org/Book/ (확인 2026-09-21) |
| 최적화·상태추정 | 비선형 최소제곱, 공분산, Lie군 위의 추정 | Barfoot *State Estimation for Robotics* 2nd ed. http://asrl.utias.utoronto.ca/~tdb/ (확인 2026-09-21) |
| 회전 표현 | 쿼터니언, 오차상태 칼만필터 | Solà https://arxiv.org/abs/1711.02508 (확인 2026-09-21) |
| 최적화 구현 | 번들조정을 직접 풀어 보기 | Ceres Solver https://github.com/ceres-solver/ceres-solver , GTSAM https://gtsam.org/ (확인 2026-09-21) |
| 데이터 엔지니어링 | 포맷 변환, 좌표변환, 배치 파이프라인 | PDAL https://pdal.org/ (확인 2026-09-21) |
| BIM·표준 | 정보관리 프로세스, IFC 스키마 | IfcOpenShell https://ifcopenshell.org/ , 국토교통부 BIM 기본지침 https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4516 † (확인 2026-09-21) |
| 드론 운용 | 국내 비행 자격 | 초경량비행장치 조종자 증명 — 만 14세 이상, 학과 70점 이상, 실기 전 항목 만족 https://www.easylaw.go.kr/CSP/CnpClsMainBtr.laf?popMenu=ov&csmSeq=1814&ccfNo=2&cciNo=3&cnpClsNo=1 † (확인 2026-09-21, 법제처 생활법령정보) |

### 5.3 1년 이상 — 세로획을 깊게, 가로획을 하나 고른다

이 시점부터는 목록을 따라가는 방식이 잘 먹히지 않는다. 4장에서 고른 조합에 따라 갈라진다.

| 방향 | 무엇을 배우나 | 자원 |
|------|---------------|------|
| 3D 딥러닝 (4.1) | 희소 컨볼루션, Point Transformer, 사전학습 | Pointcept https://github.com/Pointcept/Pointcept (확인 2026-09-21) |
| 방사휘도장 계열 (4.1) | NeRF/3DGS 학습과 한계 | nerfstudio https://docs.nerf.studio/ , 3DGS 원 구현 https://github.com/graphdeco-inria/gaussian-splatting (확인 2026-09-21) |
| BIM 정보관리 (4.2) | openBIM 표준 체계 | buildingSMART Professional Certification https://education.buildingsmart.org/ † (확인 2026-09-21) |
| 측량 국가자격 (4.2) | 응용측량, 사진측량 및 원격탐사, GIS·GNSS, 측량학 | 측량및지형공간정보기사, Q-Net http://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=1380 † (확인 2026-09-21, 한국산업인력공단) |
| 국제 자격 (4.1·4.2) | 사진측량·원격탐사·LiDAR·UAS 전문 인증 | ASPRS Certification — Scientist 등급 경력 6년, Technologist 등급 3년, Prometric 시험 https://www.asprs.org/certification (확인 2026-09-21) |
| 대용량 서비스 (4.3) | 웹 스트리밍, 옥트리 LOD | Potree https://github.com/potree/potree (확인 2026-09-21) |
| 텍스처·메시화 (공통) | 재구성 결과에 텍스처 입히기 | MVS-Texturing(BSD-3) https://github.com/nmoehrle/mvs-texturing (확인 2026-09-21) |
| 드론 매핑 자동화 (공통) | 영상에서 정사영상·DEM·점군 생성 | OpenDroneMap https://www.opendronemap.org/ (확인 2026-09-21) |

---

## 6. 손으로 해볼 실습 과제

읽는 것과 돌려 보는 것 사이의 간격이 이 분야에서 유독 크다. 아래 과제는 전부 공개 도구와 공개 데이터로 할 수 있다.

### 과제 1 — 직접 찍은 사진으로 재구성하고, 일부러 실패시켜 보기

스마트폰으로 건물 외벽이나 실내 공간을 60~120장 찍어 COLMAP으로 SfM과 MVS를 돌린다. 그다음이 본론이다. 중복도를 일부러 낮추거나, 유리·반사면을 넣거나, 조명이 바뀐 사진을 섞어 실패를 재현한다. 실패 원인을 매칭 그래프에서 확인한다.

- 도구: COLMAP https://colmap.github.io/ (확인 2026-09-21)

### 과제 2 — 정합을 직접 구현하고 실패 조건을 기록하기

Open3D로 두 점군을 복셀 다운샘플링 → FPFH 특징 → RANSAC 전역 정합 → point-to-plane ICP 순으로 맞춘다. 초기 자세를 바꿔 가며 수렴 여부를 기록하고, 왜 실패하는지 정리한다.

- 도구: Open3D https://www.open3d.org/ (확인 2026-09-21)

### 과제 3 — 3DGS를 학습시키고 레이저 스캔과 비교하기

nerfstudio의 splatfacto로 3DGS를 학습시킨 뒤, 같은 대상의 레이저 스캔 점군과 CloudCompare에서 거리를 비교한다. 앞서 인용한 연구가 지적한 평면 노이즈가 실제로 보이는지 확인한다. 자기 눈으로 확인한 한계는 남의 논문 결론보다 오래 남는다.

- 도구: nerfstudio https://docs.nerf.studio/ , CloudCompare https://www.cloudcompare.org/ (확인 2026-09-21)

### 과제 4 — 공개 데이터셋으로 실내 의미분할 학습시키기

S3DIS 또는 ScanNet으로 실내 점군 의미분할을 학습시킨다. Pointcept의 설정 파일을 그대로 쓰되, 클래스별 IoU를 뜯어보고 어떤 부재에서 성능이 무너지는지 확인한다. 벽은 잘 맞고 기둥은 안 맞는 이유를 설명할 수 있으면 성공이다.

- 데이터: Stanford 2D-3D-S / S3DIS — 3개 건물 6개 구역, 약 6,020 m², 12개 의미 클래스, 약 6.96억 점 ([Armeni 외, 2017](https://arxiv.org/abs/1702.01105), 확인 2026-09-21), 배포 페이지 http://buildingparser.stanford.edu/dataset.html †
- 데이터: ScanNet — 1,500개 이상 스캔, 250만 뷰, 인스턴스 단위 의미 라벨. 소속 기관 이메일로 이용약관에 동의한 뒤 받는다 https://github.com/ScanNet/ScanNet (확인 2026-09-21)
- 코드: Pointcept https://github.com/Pointcept/Pointcept (확인 2026-09-21)

### 과제 5 — 옥외 LiDAR로 스케일을 체감하기

항공 LiDAR 데이터로 분류 모델을 돌려 본다. 실내 데이터와 점 밀도, 클래스 불균형, 메모리 압박이 어떻게 다른지 직접 부딪쳐 보는 게 목적이다.

- 데이터: DALES — 10 km² 범위, 5억 점 이상 수작업 라벨, 8개 객체 범주 ([Varney 외, 2020](https://arxiv.org/abs/2004.11985), 확인 2026-09-21)
- 데이터: SemanticKITTI — 10 Hz로 기록한 360도 LiDAR 시퀀스에 의미·인스턴스 라벨을 붙였다 http://www.semantic-kitti.org/ (확인 2026-09-21)

### 과제 6 — 파이프라인을 자동화하고 웹에 올리기

PDAL 파이프라인으로 E57/LAS를 읽어 좌표계를 변환하고 필터링한 뒤, 타일링해서 Potree로 브라우저에 띄운다. 파일 하나를 손으로 처리하는 것과 100개를 스크립트로 처리하는 것의 차이를 몸으로 배운다.

- 도구: PDAL https://pdal.org/ , Potree https://github.com/potree/potree (확인 2026-09-21)

### 과제 7 (선택) — 재구성 정확도를 숫자로 내기

벤치마크 데이터로 자기 파이프라인의 정확도를 정량 평가한다. 레이저 스캐너 기준값이 있는 데이터를 써야 의미가 있다.

- 데이터: ETH3D — 고해상도 DSLR 다시점 스테레오 학습 13개·평가 12개 장면, 고정밀 레이저 스캐너 기준값 https://www.eth3d.net/overview (확인 2026-09-21)
- 데이터: Tanks and Temples — 실험실 밖 실제 환경에서 촬영, 산업용 레이저 스캐너 기준값 https://www.tanksandtemples.org/ (확인 2026-09-21)

---

## 7. 배우지 않아도 되는 것 / 과대평가된 것

목록을 줄이는 것도 로드맵의 일이다. 아래는 "절대 쓸모없다"가 아니라 "먼저 배울 이유가 약하다"는 뜻이다.

**특정 벤더 소프트웨어의 메뉴 구조를 먼저 외우는 일**

Leica Cyclone, Autodesk ReCap, RIEGL RiSCAN PRO는 채용 공고에 자주 등장한다([amazon.jobs](https://www.amazon.jobs/en/jobs/2503498/reality-capture-bim-engineer), 확인 2026-09-21). 그런데 같은 공고가 함께 요구하는 것은 좌표계와 측량 기준점 이해, 정합 품질관리다. 원리를 알면 UI는 며칠이면 손에 익고, 원리 없이 UI만 익히면 제품이 바뀔 때마다 처음부터 다시 시작한다(추정).

**기하 기초 없이 최신 NeRF/3DGS 논문만 따라 읽는 일**

3DGS의 공간 정확도는 입력 영상 수, 초기 점군 품질, 학습 반복 같은 조건에 크게 좌우된다([ISPRS Annals XI-M-1-2026](https://isprs-annals.copernicus.org/articles/XI-M-1-2026/31/2026/isprs-annals-XI-M-1-2026-31-2026.html), 확인 2026-09-21). 콘크리트 부재 비교 연구에서는 평면 노이즈 탓에 처짐·휨 세부가 사라졌다([Springer](https://link.springer.com/chapter/10.1007/978-981-95-8489-5_53), 확인 2026-09-21). 이런 판단을 하려면 결국 기하와 오차론으로 돌아가야 한다. 논문 편수를 늘리는 것보다 과제 3을 한 번 하는 쪽이 낫다(추정).

**고급 그래픽스 렌더링 이론**

PBR, 전역조명, 셰이더 최적화는 시각화 제품을 직접 만들 게 아니라면 우선순위가 낮다. Reality Capture에서 렌더링은 결과를 보여 주는 단계지 값을 만드는 단계가 아니다(추정).

**C++ 템플릿 메타프로그래밍 같은 언어 깊이**

PCL과 Ceres를 읽다 보면 만나게 되지만, 먼저 공부할 대상은 아니다. 남의 코드를 빌드하고 고칠 정도면 오랫동안 충분하다(추정).

**"완전 자동 scan-to-BIM이 곧 온다"는 전제로 세우는 계획**

리뷰 논문이 공통으로 지적하는 것은 주요 부재를 넘어선 객체, 가려진 영역, 라벨 데이터 부족과 도메인 갭이다([Springer 리뷰](https://link.springer.com/chapter/10.1007/978-981-92-2743-3_40), 확인 2026-09-21; [DawNet](https://www.sciencedirect.com/science/article/abs/pii/S0926580524002097), 확인 2026-09-21). 자동화를 전제로 모델링 역량을 건너뛰면 자동화 결과를 검수할 사람이 사라진다.

**시장조사 보고서의 성장률 숫자**

디지털 트윈 시장 전망치는 발행 기관과 시장 범위 정의에 따라 크게 갈린다. 건설 디지털 트윈 시장 성장률을 연 24%로 잡는 보고서가 있는가 하면([DataNext Research](https://datanextresearch.com/report/construction-digital-twin-market), 확인 2026-09-21 — 상업적 시장조사 보고서), 전체 디지털 트윈 시장은 연 40%대로 잡는 보고서도 검색된다(원문 미확인). 방향성 참고용으로는 쓸 수 있어도, 진로 결정의 근거로 삼기에는 약하다.

---

## 8. 한 줄 요약

세로획은 기하와 오차론이다. 도구는 3년이면 바뀌지만 좌표변환과 최소제곱은 안 바뀐다. 가로획은 자기가 속한 조직에 이미 자리가 있는 방향으로 그어야 연습할 기회가 생긴다.

---

## 용어 후보

용어집(`00-glossary.md`)에 올릴 만한 항목을 모았다. 정의는 한 줄로 줄였고, 확정 정의는 용어집에서 다듬는다.

- **번들조정(Bundle Adjustment)** — 여러 시점의 관측을 동시에 써서 카메라 자세와 3차원 점 좌표를 비선형 최소제곱으로 함께 보정하는 절차 — https://github.com/ceres-solver/ceres-solver (확인 2026-09-21)
- **SfM(Structure from Motion)** — 여러 장의 영상에서 카메라 자세와 희소 3차원 구조를 복원하는 기법 — https://colmap.github.io/ (확인 2026-09-21)
- **MVS(Multi-View Stereo)** — 자세가 알려진 다시점 영상에서 밀집 점군이나 메시를 만드는 기법 — https://colmap.github.io/ (확인 2026-09-21)
- **ICP(Iterative Closest Point)** — 두 점군의 대응점을 반복 갱신하며 강체변환을 추정하는 정합 알고리즘 — https://www.open3d.org/ (확인 2026-09-21)
- **오차상태 칼만필터(Error-State Kalman Filter)** — 상태 자체가 아니라 오차를 추정해 회전의 비선형성을 다루는 필터 — https://arxiv.org/abs/1711.02508 (확인 2026-09-21)
- **팩터그래프(Factor Graph)** — 변수와 제약을 이분 그래프로 표현해 SLAM·센서융합 문제를 푸는 방식 — https://gtsam.org/ (확인 2026-09-21)
- **3D Gaussian Splatting(3DGS)** — 장면을 3차원 가우시안 집합으로 표현해 실시간으로 렌더링하는 방사휘도장 기법 — https://github.com/graphdeco-inria/gaussian-splatting (확인 2026-09-21)
- **E57(ASTM E2807)** — 점 좌표·색·강도와 2D 영상을 함께 담는 벤더 중립 점군 교환 포맷, 2011년 2월 ASTM 승인 — https://paulbourke.net/dataformats/e57/ (확인 2026-09-21)
- **LAS / LAZ** — ASPRS가 정의한 LiDAR 점군 표준 포맷과 그 압축 형태 — https://paulbourke.net/dataformats/laz/LAS_1_4_r15.pdf † (확인 2026-09-21)
- **COPC(Cloud Optimized Point Cloud)** — 단일 파일 안에 옥트리로 공간 정렬해 HTTP 부분 읽기를 가능하게 한 점군 포맷 — https://lidarnews.com/cloud-optimized-point-clouds-copc/ † (확인 2026-09-21)
- **LOA(Level of Accuracy)** — USIBD가 정의한 기존 시설물 문서화 정확도 등급, LOA 10부터 LOA 50까지 — http://usibd.org/product/usibd-level-of-accuracy-loa-specification-guide-version-3-0-2019/ (확인 2026-09-21)
- **IFC(Industry Foundation Classes)** — openBIM 데이터 교환 스키마, IFC4.3이 ISO 16739-1:2024로 발행 — https://www.iso.org/standard/84123.html † (확인 2026-09-21)
- **ISO 19650** — 건설 자산 생애주기 정보관리 국제표준 시리즈 — https://www.iso.org/standard/68078.html † (확인 2026-09-21)
- **KGD2002(한국측지계 2002)** — GRS80 타원체와 ITRF2000 데이텀에 기반한 대한민국 세계측지계 성과 — https://www.ngii.go.kr/other/file_down.do?sq=101741 † (확인 2026-09-21)
- **GSD(Ground Sample Distance)** — 영상 한 픽셀이 대응하는 지상 거리, 촬영 계획과 기대 정확도를 잇는 값 — https://www.ipb.uni-bonn.de/photogrammetry-i-ii/ (확인 2026-09-21)
- **도메인 갭(Domain Gap)** — 학습 데이터와 실제 데이터의 분포 차이로 성능이 떨어지는 현상, 합성 점군 학습의 주요 장애 — https://www.sciencedirect.com/science/article/abs/pii/S0926580524002097 (확인 2026-09-21)
