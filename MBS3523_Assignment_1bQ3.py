import cv2
import numpy as np

cam =cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret, frame = cam.read()


    flipped_vertical = cv2.flip(frame, 0)
    flipped_horizontal = cv2.flip(frame, 1)
    flipped_both = cv2.flip(frame, -1)
    top_row = np.hstack((frame, flipped_horizontal))
    bottom_row = np.hstack((flipped_vertical, flipped_both))
    combined = np.vstack((top_row, bottom_row))

    cv2.imshow('Webcam Frame Orientations', combined)


    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()