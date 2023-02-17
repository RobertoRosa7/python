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

box_config = {
    'w_min': 40,
    'h_min': 40,
    'offset': 2,
    'line_roi': 620,  # counter position line
    'car': 0
}

cap = cv2.VideoCapture(PONTE_VIDEO)
detec = []


def centroides(x, y, w, h):
    x1 = w // 2
    y1 = y // 2
    cx = x + x1
    cy = y + y1

    return cx, cy


def set_info(detec, frame):
    for (x, y) in detec:
        if ((box_config['line_roi'] + box_config['offset']) > y > (box_config['line_roi'] - box_config['offset'])):
            box_config['car'] += 1
            cv2.line(frame, (25, box_config['line_roi']), (1200, box_config['line_roi']), (0, 127, 255), 3)
            detec.remove((x, y))
            print(f'Carros detectados até o momento: {str(box_config["car"])}')


def show_info(frame, mask):
    text = f'Carros: {box_config["car"]}'
    cv2.putText(frame, text, (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Video Original", frame)
    # cv2.imshow("Detectar", mask)


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


while True:
    ok, frame = cap.read()

    if not ok:
        print('No Frames')
        break

    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    mask = substractor('GMG').apply(frame)
    mask = filter(mask, 'combine')

    contorno, img = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame, (25, box_config['line_roi']), (1200, box_config['line_roi']), (255, 127, 0), 3)

    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= box_config['w_min']) and (h >= box_config['h_min'])

        if not validar_contorno:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = centroides(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame, centro, 4, (0, 0, 255), -1)

        set_info(detec, frame)
        show_info(frame, mask)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
