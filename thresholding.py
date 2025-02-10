import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('dog.jpg')
cv.imshow('dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# # simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold invers', thresh_inv)

# Adaptive thresholdig
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold invers', adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adaptive threshold invers', adaptive_thresh_inv)
 
cv.waitKey(0)