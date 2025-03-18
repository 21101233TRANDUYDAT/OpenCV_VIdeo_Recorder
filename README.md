# OpenCV를 활용한 다각형 영역 비디오 녹화

이 프로젝트는 OpenCV를 사용하여 웹캠을 통해 다각형 영역을 지정하고, 해당 영역을 기반으로 비디오를 녹화하거나 이미지를 캡처하는 기능을 포함합니다.

## 📂 폴더 구조
프로그램 실행 시 다음과 같은 폴더가 자동으로 생성됩니다:
- `video` 📁: 녹화된 비디오 파일이 저장되는 폴더  
- `Image_ex` 📁: 캡처된 이미지가 저장되는 폴더  

---

## 🛠️ 기능 설명

### 1. 비디오 녹화 및 이미지 캡처
- **비디오 녹화 시작/중지**  
  - `Space (스페이스바)` 키를 눌러 녹화를 시작하거나 중지할 수 있습니다.  
  - 비디오 파일은 `video` 폴더에 `out_put_videoX.avi` 형식으로 저장됩니다.  

- **다각형 영역 이미지 캡처**  
  - `c` 키를 누르면 그린 다각형 영역 내부의 이미지를 캡처합니다.  
  - 캡처된 이미지는 `Image_ex` 폴더에 `out_put_ImageX.jpg` 형식으로 저장됩니다.  

---

### 2. 다각형 그리기 및 관리
- **점 추가**  
  - **마우스 왼쪽 클릭**으로 다각형을 만들 점을 추가할 수 있습니다.  

- **마지막 점과 첫 번째 점 연결**  
  - `d` 키를 누르면 마지막 점과 첫 번째 점이 자동으로 연결됩니다.  

- **그린 다각형 초기화**  
  - `r` 키를 누르면 기존에 그린 모든 점이 초기화되어 다시 그릴 수 있습니다.  

---

### 3. 상태 및 FPS 표시
- **FPS(Frame Per Second) 표시**  
  - 현재 웹캠의 FPS 값이 화면 오른쪽 상단에 표시됩니다.  

- **녹화 상태 표시**  
  - `Recording` (녹화 중)일 때는 빨간색 원과 텍스트가 표시됩니다.  
  - `Preview` (미리보기) 상태일 때는 파란색 원과 텍스트가 표시됩니다.  

---

### 4. 프로그램 종료
- `Esc (ESC 키)` 를 누르면 프로그램이 종료됩니다.  

---

## 실행 방법
1. Python과 OpenCV가 설치되어 있어야 합니다.
   ```bash
   pip install opencv-python numpy
