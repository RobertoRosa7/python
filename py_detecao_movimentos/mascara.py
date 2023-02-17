import cv2
import sys

PATH_VIDEO = r'D:\Databases\Videos'
PONTE_VIDEO = PATH_VIDEO + r'\Ponte.mp4'

algorithm_types = {
    'KNN': cv2.createBackgroundSubtractorKNN(),
    'GMG': cv2.bgsegm.createBackgroundSubtractorGMG(),
    'CNT': cv2.bgsegm.createBackgroundSubtractorCNT(),
    'MOG': cv2.bgsegm.createBackgroundSubtractorMOG(),
    'MOG2': cv2.createBackgroundSubtractorMOG2()
}
e1 = cv2.getTickCount()


# time KNN - 5.136
# time GMG - 8.827
# time CNT - 4.048
# time MOG - 6.273
# time MOG2 - 4.788
def substractor(algorithm_type):
    try:
        return algorithm_types[algorithm_type]
    except Exception:
        sys.exit(1)


cap = cv2.VideoCapture(PONTE_VIDEO)
# background_subtractor = substractor('MOG2')

substractor_list = []
for sub in algorithm_types:
    substractor_list.append(substractor(sub))


def main():
    while (cap.isOpened):
        ok, frame = cap.read()

        if not ok:
            print('No Frames')
            break

        frame = cv2.resize(frame, (0, 0), fx=0.35, fy=0.35)

        knn = substractor_list[0].apply(frame)
        gmg = substractor_list[1].apply(frame)
        cnt = substractor_list[2].apply(frame)
        mog = substractor_list[3].apply(frame)
        mog2 = substractor_list[4].apply(frame)

        cv2.imshow('Original', frame)
        cv2.imshow('KNN', knn)
        cv2.imshow('GMG', gmg)
        cv2.imshow('CNT', cnt)
        cv2.imshow('MOG', mog)
        cv2.imshow('MOG2', mog2)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    e2 = cv2.getTickCount()
    t = (e2 - e1) / cv2.getTickFrequency()

    print(f'Freq: {t}')


main()
