import cv2 as cv

# read image
img = cv.imread("dog.jpg")
cv.imshow('dog', img)
cv.waitKey(0)

# reading video
capture = cv.VideoCapture("catvdo.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow("video" , frame)

    if cv.waitkey(00) & 0xFF==ord('d'):
        break
     
    capture.release()
    cv.destroyAllWindows()

