#평균 필터(blur)

import cv2
import numpy as np

def mean_blur(img):
    bin_array = np.zeros(img.shape,dtype=np.uint8)
    height, width = img.shape
    for y in range(height):
        for x in range(width):
            try:
                value = (int(img[y - 1, x - 1]) + int(img[y - 1, x]) + int(img[y - 1, x + 1]) +int(img[y, x - 1]) + int(img[y, x]) + int(img[y, x + 1]) + int(img[y + 1, x - 1]) + int(img[y + 1, x]) + int(img[y + 1, x + 1]))
                value = int(value/9)
                if value > 255:
                    bin_array[y,x] = 255
                elif value < 0:
                    bin_array[y,x] = 0
                else :
                    bin_array[y,x] = int(value)
            except:
                pass
    return bin_array

lena_gray = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
lena_blur = mean_blur(lena_gray)
cv2.imshow("lena", lena_gray)
cv2.imshow("lena blur", lena_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 평균 필터 직접 구현한 버전
# import cv2
# import numpy as np
#
# def mean_blur(img):
#     dst = np.zeros(img.shape, dtype=np.uint8)
#     height, width = img.shape
#
#     for y in range(1, height - 1):
#         for x in range(1, width - 1):
#             region = img[y-1:y+2, x-1:x+2]
#             value = np.mean(region)
#             dst[y, x] = int(value)
#
#     return dst
#
# lena_gray = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Lena", lena_gray)
# cv2.imshow("Mean Blur", mean_blur(lena_gray))
# cv2.waitKey()
# cv2.destroyAllWindows()