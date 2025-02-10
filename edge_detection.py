import cv2 as cv
import numpy as np

img = cv.imread('lady.png')
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# performing edge detection
gradients_sobelx = cv.Sobel(gray, -1, 1, 0)
gradients_sobely = cv.Sobel(gray, -1, 0, 1)
gradients_sobelxy = cv.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5,0)
gradients_laplacian = cv.Laplacian(gray, -1)
canny_output = cv.Canny(gray, 80, 150) 


cv.imshow('sobel x', gradients_sobelx)
cv.imshow('sobel y', gradients_sobely)
cv.imshow('sobel x+y', gradients_sobelxy)
cv.imshow('laplacian', gradients_laplacian)
cv.imshow('Canny', canny_output)


cv.waitKey(0)