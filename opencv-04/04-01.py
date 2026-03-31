import cv2
import numpy as np

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
shape = cv2.imread('shape.png', cv2.IMREAD_GRAYSCALE)

# dx=1, dy=0: 수직 에지 검출
sobel_x = cv2.Sobel(img, -1, 1, 0, ksize=3)

# dx=0, dy=1: 수평 에지 검출
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize=3)

edges1 = cv2.Canny(img, 50, 100)
edges2 = cv2.Canny(img, 50, 200)
edges = cv2.Canny(img, 100, 200)
shape_edges = cv2.Canny(shape, 100, 200)

# Canny 에지 이미지에서 직선 검출
lines = cv2.HoughLinesP(edges1, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
dst = cv2.cvtColor(edges1, cv2.COLOR_GRAY2BGR) # 컬러로 변환해 그리기
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
circles = cv2.HoughCircles(shape_edges, cv2.HOUGH_GRADIENT, dp=1, minDist = 20, param1=100, param2=30, minRadius = 10, maxRadius = 100)
shape_dst = cv2.cvtColor(shape_edges, cv2.COLOR_GRAY2BGR)
if circles is not None:
    for circle in circles:
        x, y, r = circle[0]
        cv2.circle(shape_dst, (int(x), int(y)), int(r), (0, 0, 255), 2)

cv2.imshow('shape',shape_edges)
cv2.imshow('shape_dst',shape_dst)
cv2.imshow('dst', dst)
cv2.imshow('Canny Edge1', edges1)
cv2.imshow('Canny Edge2', edges2)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 허프 원 검출
# import cv2
# import numpy as np
#
# src = cv2.imread('shape.png')
# gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# circles1 = cv2.HoughCircles(gray, dp=1, minDist=50, param2=15)
#
# circles1 =  np.int32(circles1)
# print('circles1.shape=', circles1.shape)
# for circle in circles1[0,:]:
#     cx, cy, r  = circle
#     cv2.circle(src, (cx, cy), r, (0,0,255), 2)
# cv2.imshow('src',  src)
#
# cv2.waitKey()
# cv2.destroyAllWindows()