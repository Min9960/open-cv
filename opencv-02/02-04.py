import cv2

src = cv2.imread("lena.jpg")
b, g, r = cv2.split(src) # 채널 분리
dst = cv2.merge((r, b, g)) # 채널 병합

# 번외: HSV 변환 (채도, 명도 조절 용이)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow("src",src)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("dst",dst)
cv2.imshow("hsv",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()