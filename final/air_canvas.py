import cv2
import numpy as np
import random
cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)
kernel = np.ones((5, 5), np.uint8)
# 빨간색 추출 예시 (H: 0~10 or 170~180)
# 빨간색은 Hue 값이 0 근처와 180 근처 양쪽에 걸쳐 있습니다.
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([179, 255, 255])
color = (0, 0, 255)

if not cap.isOpened():
    print("Camera open failed!")
    exit()
else :
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    bin_frame = np.zeros((prev_frame.shape[0], prev_frame.shape[1]), dtype=np.uint8)

while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)
    _, diff_thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    target = cv2.bitwise_and(mask,diff_thresh)
    bin_frame[target == 255] = 255
    frame[bin_frame == 255] = color
    cv2.imshow('frame', frame)
    key = cv2.waitKey(10)
    if key == 27:  # ESC 키
        break
    elif key == ord('c'):
        bin_frame = np.zeros((prev_frame.shape[0], prev_frame.shape[1]), dtype=np.uint8)
    elif key == ord('p'):
        color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    else :
        prev_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()