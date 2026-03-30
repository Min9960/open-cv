import cv2
import numpy as np
help(cv2.filter2D)

lena_gray = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
sharpening_mask = np.array([[-1, -1, -1],
                            [-1,  9, -1],
                            [-1, -1, -1]])
sharpening_mask2 = np.array([[-0.5, 0.5, -0.5],
                            [0.5,  1, 0.5],
                            [-0.5, 0.5, -0.5]])
dst_sharp = cv2.filter2D(lena_gray, -1, sharpening_mask)
dst_sharp2 = cv2.filter2D(lena_gray, -1, sharpening_mask2)
cv2.imshow("lena", lena_gray)
cv2.imshow("sharp1", dst_sharp)
cv2.imshow("sharp2", dst_sharp2)
cv2.waitKey(0)
cv2.destroyAllWindows()