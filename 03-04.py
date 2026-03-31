# 아핀 변환
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lena.jpg')

rows, cols, channels = img.shape
arr1 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
arr2 = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 1.2)
dst1 = cv2.warpAffine(img, arr1, (cols, rows))
dst2 = cv2.warpAffine(img, arr2, (cols, rows))
pts1 = np.float32([[200, 100], [400, 100], [200,200]])
pts2 = np.float32([[200, 300], [400, 200], [200,400]])

cv2.circle(img,(200,100),10,(255,0,0),-1)
cv2.circle(img,(400,100),10,(0,255,0),-1)
cv2.circle(img,(200,200),10,(0,0,255),-1)

M = cv2.getAffineTransform(pts1,pts2)
dst3 = cv2.warpAffine(img,M,(cols,rows))


cv2.imshow("lena3", dst1)
cv2.imshow("lena2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(121),plt.imshow(img),plt.title('Image')
plt.subplot(122),plt.imshow(dst3),plt.title('dst3')
plt.show()