import cv2
import numpy as np

src = cv2.imread('rail.jpg')
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
print(src.shape)

dst_gaussian = cv2.GaussianBlur(src, (3, 3), 0)
edges = cv2.Canny(dst_gaussian, 160, 210)
lines = cv2.HoughLinesP(edges, 1, np.pi/100, 100, minLineLength=200, maxLineGap=40)
src = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
dst_gaussian = cv2.cvtColor(dst_gaussian, cv2.COLOR_GRAY2BGR)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst_gaussian, (x1, y1), (x2, y2), (0, 0, 255), 3)


cv2.imshow('Original', src)
cv2.imshow('Gaussian', dst_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
