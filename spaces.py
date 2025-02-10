import cv2 as cv

img = cv.imread('badminton.jpg')
cv.imshow('badminton', img)

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# HSV
HSV = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('HSV', HSV)

# L+a+b
Lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', Lab)
 
# RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)


cv.waitKey(0)
