import cv2 as cv

img = cv.imread('dog.jpg')
cv.imshow('dog', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray' ,gray)

# blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_CONSTANT)
cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow('edge', canny) 

# dilating image
dilate = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('dilate',dilate)

# erating
eroded = cv.erode(dilate,(3,3),iterations=1 )
cv.imshow('reoding',eroded)

# resize                                           
resized = cv.resize(img,(500,500))
cv.imshow('resize',resized)

cv.waitKey(0)


