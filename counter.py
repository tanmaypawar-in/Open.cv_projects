import cv2 as cv

img = cv.imread('badminton.jpg')
cv.imshow('badminton', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# find

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#draw

img_copy = img.copy()
img_copy = cv.drawContours(img_copy, contours, -1, (0,255,0), thickness=2)
 
cv.imshow('draw_counter', img_copy)

 
cv.waitKey(0) 