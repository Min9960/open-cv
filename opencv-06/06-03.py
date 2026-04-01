import cv2
cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break

    cv2.imshow('Camera', frame)
    if cv2.waitKey(10) == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()