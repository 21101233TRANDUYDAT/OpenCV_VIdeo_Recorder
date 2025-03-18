import cv2

source = 'video/out_put_video2.avi'
cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print('cant open camera!')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print('cant receive frame! Exiting....')

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break