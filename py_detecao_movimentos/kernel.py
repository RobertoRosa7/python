import numpy as np
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

kernel_types = {
    'dilation': cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)),
    'opening': np.ones((3, 3), np.uint8),
    'closing': np.ones((3, 3), np.uint8)
}

cap = cv2.VideoCapture(PONTE_VIDEO)


def substractor(type):
    try:
        return algorithm_types[type]
    except Exception:
        sys.exit(1)


def kernel(type):
    try:
        return kernel_types[type]
    except Exception:
        sys.exit(1)


def closing(img):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel('closing'), iterations=2)


def opening(img):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel('opening'), iterations=2)


def dilation(img):
    return cv2.dilate(img, kernel('dilation'), iterations=2)


def combine(img):
    return dilation(opening(closing(img)))


filter_types = {
    'closing': closing,
    'opening': opening,
    'dilation': dilation,
    'combine': combine
}


def filter(img, type):
    try:
        return filter_types[type](img)
    except Exception:
        sys.exit(1)


def main():
    while (cap.isOpened):
        ok, frame = cap.read()

        if not ok:
            print('No Frames')
            break

        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        mask = substractor('GMG').apply(frame)
        mas_filter = filter(mask, 'combine')
        cars_after_mask = cv2.bitwise_and(frame, frame, mask=mas_filter)

        cv2.imshow('Original', frame)
        cv2.imshow('GMG', cars_after_mask)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break


# print(f"dilation:\n{kernel('dilation')}")
# print(f"open:\n{kernel('opening')}")
# print(f"close:\n{kernel('closing')}")

main()
