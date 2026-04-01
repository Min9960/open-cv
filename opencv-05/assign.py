import cv2
import matplotlib.pyplot as plt
import numpy as np

src = cv2.imread("coins.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cols, rows = gray.shape
print(gray.shape)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
_, thresh =  cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=2)
erosion = cv2.erode(dilation, kernel, iterations=3)

contours, hierachy = \
cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.drawContours(src, contours, -1, (0, 0, 255), 3)

coins = len(contours)
text = f"found {coins} coins"

cv2.putText(src, text, org = (int(rows/3.3), int(cols/2)), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (255, 0, 0)
, thickness = 2)
cv2.imshow('src',src)
cv2.imshow('thresh', thresh)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread('coins.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (11, 11), 0)
#
# _, thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)
#
# kernel = np.ones((3, 3), np.uint8)
# closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
#
# contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# result = img.copy()
# cv2.drawContours(result, contours, -1, (0, 255, 0), 3)
#
# text = f"found {len(contours)} coins"
# cv2.putText(result, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#
# cv2.imshow('Coin Counter', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()