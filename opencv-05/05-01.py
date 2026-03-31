from unittest import result

import cv2
import numpy as np

src = cv2.imread('lena.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
img = cv2.imread('morphology.jpg', cv2.IMREAD_GRAYSCALE)

# 빨간색 추출 예시 (H: 0~10 or 170~180)
# 빨간색은 Hue 값이 0 근처와 180 근처 양쪽에 걸쳐 있습니다.
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
src = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src) # 그레이스케일 영상 전용

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
result1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
result2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('open', result1)
cv2.imshow('close', result2)
cv2.imshow('Source', src)
cv2.imshow('Equalized', dst)
cv2.imshow('Red Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
