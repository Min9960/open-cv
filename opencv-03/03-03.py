import cv2
img = cv2.imread('lena.jpg')
dst1 = cv2.resize(img,(1024,1024), interpolation = cv2.INTER_AREA)
dst2 = cv2.resize(img,(1024,1024), interpolation = cv2.INTER_CUBIC)
dst3 = cv2.resize(img,(1024,1024), interpolation = cv2.INTER_LINEAR)

cv2.imshow("lena1", dst1)
cv2.imshow("lena2", dst2)
cv2.imshow("lena3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()