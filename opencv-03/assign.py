import cv2
import numpy as np

src = cv2.imread('resume.jpg')
src = cv2.resize(src,None,fx=0.2,fy=0.2,interpolation = cv2.INTER_AREA)
cols,rows = src.shape[:2]

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("오른쪽 버튼 더블 클릭:", x, y)
pts1 = np.float32([[63, 127], [517, 118], [527,763]])
pts2 = np.float32([[0, 0], [450, 0], [450,650]])
pts3 = np.float32([[63, 127], [517, 118], [527,763], [70,771]])
pts4 = np.float32([[0, 0], [450, 0], [450,650], [0,650]])

M1 = cv2.getAffineTransform(pts1,pts2)
dst1 = cv2.warpAffine(src,M1,(450,650))
M2 = cv2.getPerspectiveTransform(pts3,pts4)
dst2 = cv2.warpPerspective(src,M2,(450,650))

cv2.imshow('src', src)
cv2.setMouseCallback('src', mouse_callback)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# practice-easy.py
# 정해진 이미지의 정해진 좌표값을 하드코딩하는 방식
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# src = cv2.imread("book.jpg")
# rows, cols, ch = src.shape
#
# # x, y 순서로 좌표 쓰면 됨
# pts1 = np.float32([
#     [57, 24],
#     [416, 14],
#     [16, 528],
#     [467, 522]])
# pts2 = np.float32([
#     [0,0],
#     [cols,0],
#     [0,rows],
#     [cols, rows]])
#
# cv2.circle(src, (57, 24), 10, (255,0,0),-1)
# cv2.circle(src, (416, 14), 10, (0,255,0),-1)
# cv2.circle(src, (16, 528), 10, (0,0,255),-1)
# cv2.circle(src, (467, 522), 10, (255,0,255),-1)
#
# M = cv2.getPerspectiveTransform(pts1, pts2)
# dst = cv2.warpPerspective(src, M, (cols,rows))
#
# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# practice-hard.py
# 직접 마우스 클릭으로 좌표를 지정하면, 알아서 원근법을 적용하는 방식
# import cv2
# import numpy as np
#
# points1 = np.zeros((4,2), dtype=np.float32)
# count = 0 # 클릭 횟수를 센다
#
# img = cv2.imread("book.jpg")
# rows, cols, ch = img.shape
#
# # 클릭해둔 좌표가 이동할 목적 좌표
# points2 = np.float32([
#     [0,0],
#     [cols,0],
#     [0,rows],
#     [cols, rows]])
#
# # 마우스 클릭시 클릭한 위치의 좌표를 배열에 추가하는 이벤트 리스너
# def mouseHandler(event, x, y, flags, param):
#     global points
#     global count
#     if event==cv2.EVENT_LBUTTONDOWN:
#         points1[count] = [x, y]
#         count += 1
#         cv2.circle(img, (x,y), 5, (0, 0, 255), -1) #반지름 5크기 빨간 점
#         cv2.imshow("img", img)
#         if count == 4 :
#             M = cv2.getPerspectiveTransform(points1, points2)
#             dst = cv2.warpPerspective(img, M, (cols,rows))
#             cv2.imshow("dst", dst)
#
#
# cv2.imshow("img", img)
# cv2.setMouseCallback("img", mouseHandler)
# cv2.waitKey(0)
# cv2.destroyAllWindows()