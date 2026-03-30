import cv2
import numpy as np
import sys

drawing = False
brush_size = 5

def mouse_callback(event, x, y, flags, param):
    global drawing, canvas, brush_size
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # 원을 계속 찍어서 선처럼 보이게
            cv2.circle(canvas, (x, y), brush_size, (0, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)

while True:
    cv2.imshow('Canvas', canvas)
    cv2.setMouseCallback('Canvas', mouse_callback)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('c'):
        canvas[:] = 255
    elif key == ord('+'):
        brush_size += 1
        print("브러시 크기:", brush_size)
    elif key == ord('-') and brush_size > 1:
        brush_size -= 1
        print("브러시 크기:", brush_size)

# import cv2
# import numpy as np
#
# canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
# 
#
# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         if flags == cv2.EVENT_FLAG_LBUTTON:
#             cv2.circle(canvas, (x, y), 3, (0, 0, 0), -1)
#
#
# while True:
#     cv2.imshow('Canvas', canvas)
#     cv2.setMouseCallback('Canvas', mouse_callback)
#     key = cv2.waitKey(10)
#     if key == ord('c'):
#         canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
#     elif key == ord('q') or key == 27:
#         break
#
# cv2.destroyAllWindows()