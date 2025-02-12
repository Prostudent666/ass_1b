import cv2

cam =cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret, frame = cam.read()
    frameResize = cv2.resize(frame, (480, 360))
    blurred = cv2.GaussianBlur(frameResize, (15, 15), 0)
    hsv = cv2.cvtColor(frameResize, cv2.COLOR_BGR2HSV)
    edges = cv2.Canny(frameResize, 100, 200)
    cv2.imshow('Original Image', frameResize)
    cv2.imshow('Gaussian Blur', blurred)
    cv2.imshow('HSV Color Space', hsv)
    cv2.imshow('Canny Edges', edges)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
