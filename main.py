import cv2
import os
import numpy as np

#make folder if not exists
outPut_Video_folder = 'video'
if not os.path.exists(outPut_Video_folder):
    os.mkdir(outPut_Video_folder)
outPut_Image_folder = 'Image_ex'
if not os.path.exists(outPut_Image_folder):
    os.mkdir(outPut_Image_folder)

#val
is_recording = False
out = None
count_video = 0
count_image = 0
frame_count = 0
points = []

#Mouse function
def left_mouse_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon(frame, points):
    for point in points:
         cv2.circle(frame, (point[0], point[1]), 5, (0, 0, 255), -1)
    frame = cv2.polylines(frame, [np.int32(points)], False, (0, 0, 255), 2)
    return frame


#video process
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('can not open camera!')
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (width, height)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Can not receive frame (stream end?). Exiting ...')
        break

    frame = cv2.flip(frame, 1)
    frame = draw_polygon(frame, points)

    if is_recording:
        frame_count += 1
        status = 'Recording'
        color = (0, 0, 255)
        color_circle = (0, 0, 255)
        if frame_count % 5 == 0:
            # draw circle and status
            cv2.circle(frame, (25, 50), 20, color_circle, -1)
            cv2.putText(frame, status, (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
        out.write(frame)

    else:
        status = 'Preview'
        color = (255, 0, 0)
        color_circle = (255, 0, 0)
        # draw circle and status
        cv2.circle(frame, (25, 50), 20, color_circle, -1)
        cv2.putText(frame, status, (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)


    #puttext fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    text = f'FPS: {fps:.2f}'
    cv2.putText(frame, text, (1050, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow('frame', frame)
    '''
    key process:
    space: to change preview mode and recording mode
    'd' : connect the last point of the polygon to the first point
    'r' : reset points to draw again
    'c' : to capture image within polygon
    'esc' : to close win name
    '''
    key = cv2.waitKey(1) & 0xFF
    #recording
    if key == ord(' '):
        if is_recording:
            is_recording = False
            out.release()
            out = None
        else:
            is_recording = True
            fourcc = cv2.VideoWriter.fourcc('X', 'V', 'I', 'D')
            count_video = len(os.listdir(outPut_Video_folder))
            out = cv2.VideoWriter(os.path.join(outPut_Video_folder,f'out_put_video{count_video + 1}.avi'), fourcc, 30, frame_size, isColor=True)
            print(f'out_put_Video{count_video + 1}.jpg save successful! to {outPut_Video_folder}')

    #polygon
    elif key == ord('d') and len(points) > 2:
        points.append(points[0])

    elif key == ord('r'):
        points.clear()
        print("Reset points, ready to draw again!")

    elif key == ord('c') and len(points) > 2:
        mask = np.zeros_like(frame, dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], (255, 255, 255))

        x1 = min(point[0] for point in points)
        x2 = max(point[0] for point in points)
        y1 = min(point[1] for point in points)
        y2 = max(point[1] for point in points)
        # cropped_image = frame[y1:y2, x1:x2]
        cropped_image = cv2.bitwise_and(frame, mask)
        count_image = len(os.listdir(outPut_Image_folder))
        cv2.imwrite(os.path.join(outPut_Image_folder, f'out_put_Image{count_image + 1}.jpg'), cropped_image)
        print(f'out_put_Image{count_image + 1}.jpg save successful to {outPut_Image_folder}!')

    elif key == 27:
        break

    cv2.setMouseCallback('frame', left_mouse_click, points)

cap.release()
cv2.destroyAllWindows()