import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('dog.jpg')
cv.imshow('dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [100], [0,100])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixles')
plt.xlim([0,100])
plt.show()


cv.waitKey(0)