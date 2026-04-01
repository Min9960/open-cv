import cv2
cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

mask = cv2.imread('tigermask.png', cv2.IMREAD_UNCHANGED)
mask_x, mask_y = mask.shape[:2]
mask = mask[100:540,100:433,:]
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        x, y, w, h = None, None, None, None
    elif len(faces) > 0:
        x, y, w, h = faces[0]
        mask_sized = cv2.resize(mask, (w,h))
        alpha = mask_sized[:, :, 3] / 255.0
        alpha = alpha[:, :, None]  # (h,w) → (h,w,1)

        roi = frame[y:y + h, x:x + w]

        # float로 변환 후 연산
        blended = (alpha * mask_sized[:, :, :3] +
                       (1 - alpha) * roi)

        frame[y:y + h, x:x + w] = blended.astype('uint8')
    cv2.imshow('Camera', frame)
    if cv2.waitKey(10) == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()

# import cv2
# import sys
#
# cap = cv2.VideoCapture(0)
# sticker = cv2.imread("tigermask.png", cv2.IMREAD_UNCHANGED)
#
##pre-trained(기학습) 모델 생성
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# )
#
# def overlay_transparent(background, overlay, x, y):
#     h, w, _ = background.shape
#     ol_h, ol_w, _ = overlay.shape
# 
#     if x >= w or y >= h:
#         return background
#
#     if x + ol_w > w:
#         ol_w = w - x
#         overlay = overlay[:, :ol_w]
#
#     if y + ol_h > h:
#         ol_h = h - y
#         overlay = overlay[:ol_h]
#
#     if x < 0:
#         overlay = overlay[:, -x:]
#         ol_w = overlay.shape[1]
#         x = 0
#
#     if y < 0:
#         overlay = overlay[-y:, :]
#         ol_h = overlay.shape[0]
#         y = 0
#
#     alpha = overlay[:, :, 3] / 255.0
#     overlay_img = overlay[:, :, :3]
#
#     for c in range(3):
#         background[y:y+ol_h, x:x+ol_w, c] = (
#             overlay_img[:, :, c] * alpha +
#             background[y:y+ol_h, x:x+ol_w, c] * (1.0 - alpha)
#         )
#
#     return background
#
#
# if cap.isOpened():
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         faces = face_cascade.detectMultiScale(
#             gray,
#             scaleFactor=1.1,
#             minNeighbors=5
#         )
#
#         for (x, y, w, h) in faces:
#             sticker_resized = cv2.resize(
#                 sticker,
#                 (int(2.2 * w), int(2.2 * h))
#             )
#
#             new_x = x - int(0.6 * w)
#             new_y = y - int(0.4 * h)
#
#             frame = overlay_transparent(frame, sticker_resized, new_x, new_y)
#
#         cv2.imshow("frame", frame)
#
#         if cv2.waitKey(20) == 27:
#             break
# else:
#     sys.exit()
#
# cap.release()
# cv2.destroyAllWindows()