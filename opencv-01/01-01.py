import cv2
import numpy as np
import sys
print(cv2.__version__)

# 이미지 불러오기
img = cv2.imread('../lena.jpg')

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("오른쪽 버튼 더블 클릭:", x, y)


if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

blue = img[100,100,0]
green = img[100,100,1]
red = img[100,100,2]

img[98:100,98:100] = [0,0,0]

# 흰색 배경 생성 (512x512)
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

# 그리기
cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 5)          # 파란 선
cv2.rectangle(canvas, (50, 200), (200, 400), (0, 255, 0), -1) # 초록 꽉 찬 사각형
cv2.circle(canvas, (350, 300), 100, (0, 0, 255), 3)           # 빨간 원

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.setMouseCallback('WindowName', mouse_callback)
cv2.destroyAllWindows()



print("r, g, b", red, green, blue)

cv2.imshow('Lena Window', img)  # 윈도우 창 제목, 이미지 객체

# 키 입력 대기 (아무 키나 누르면 종료)
cv2.waitKey(0) # 매개변수에 0 넣으면 무한정 대기, 0이 아닌 양수는 대기 시간 지정, 1은 루프 안에서 처리할 때 쓰임
cv2.destroyAllWindows()