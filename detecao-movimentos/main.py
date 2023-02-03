import numpy as np
import cv2
from time import sleep

PATH_VIDEO = r'D:\Databases\Videos'
RUA_VIDEO = PATH_VIDEO + r'\Rua.mp4'
ARCO_VIDEO = PATH_VIDEO + r'\Arco.mp4'
ESTRADA_VIDEO = PATH_VIDEO + r'\Estrada.mp4'
PEIXES_VIDEO = PATH_VIDEO + r'\Peixes.mp4'
DELAY = 10

cap = cv2.VideoCapture(RUA_VIDEO)

has_frame, frame = cap.read()
frame_ids = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []

for fid in frame_ids:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    has_frame, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(dtype=np.uint8)

# print(median_frame)
# cv2.imshow('Median Frame', median_frame)
# cv2.waitKey(0)
# cv2.imwrite('Median-Frame.jpg', median_frame)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_median_frame = cv2.cvtColor(median_frame, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Median Frame', gray_median_frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(PONTE_VIDEO)

while (True):
    tempo = float(1 / DELAY)
    sleep(tempo)
    has_frame, frame = cap.read()
    if not has_frame:
        print('Acabou os frames')
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dframe = cv2.absdiff(frame_gray, gray_median_frame)
    th, dframe = cv2.threshold(dframe, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('Frame', dframe)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
