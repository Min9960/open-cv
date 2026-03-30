# 오픈소스 이미지 사이트 픽사베이에서 이미지 참고
from importlib.metadata import pass_none

import cv2

src1 = cv2.imread("lena.jpg")
src2 = cv2.imread("chroma.jpg")
src2 = cv2.resize(src2, None, fx=0.125, fy=0.125, interpolation=cv2.INTER_AREA)
src2 = cv2.resize(src2, dsize=(512,512), interpolation=cv2.INTER_LINEAR)
print(src1.shape)
print(src2.shape)
b, g, r = cv2.split(src2)
dst = src2
result = src1
for i in range(512):
    for j in range(512):
        if g[i,j] >=130 and b[i,j] <= 80 and r[i,j] <= 80:
            g[i,j] = 0
        else:
            g[i,j] = 1
for i in range(512):
    for j in range(512):
        if g[i,j] == 0:
            dst[i,j] = [0,0,0]
        else:
            pass
for i in range(512):
    for j in range(512):
        if g[i,j] == 0:    # dst[i,j] == [0,0,0]: 했는데 안됨 물어보기
            result[i,j] = src1[i,j]
        else:
            result[i,j] = src2[i,j]

cv2.imshow("src",result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # 사이즈가 다르면 연산 시 오류가 발생할 수 있다.
# src = cv2.imread('chroma.jpg')
# src = cv2.resize(src, (512, 512))
# lena = cv2.imread('lena.jpg')
#
# # 초록 배경에 해당하는 영역만 따로 누끼따기
# green_mask = cv2.inRange(src, (0, 120, 0), (100, 255, 100))
# mask_fg = green_mask # 초록색 부분만 하얗게 강조
# mask_bg = cv2.bitwise_not(mask_fg) # 초록색 부분 외의 영역을 하얗게 강조
#
# src_fg = cv2.bitwise_and(src, src, mask=mask_bg) # 초록색 외 부분과 아저씨가 겹치는 부분 AND
# lena_bg = cv2.bitwise_and(lena, lena, mask=mask_fg) # 초록색 부분과 레나가 겹치는 부분 AND
#
# result = src_fg + lena_bg
#
# cv2.imshow("src_fg", src_fg)
# cv2.imshow("lena_bg", lena_bg)
# cv2.imshow("result", result)
# cv2.waitKey()
# cv2.destroyAllWindows()