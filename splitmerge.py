import cv2 as cv
import numpy as np

img = cv.imread('badminton.jpg')
cv.imshow('badminton', img)

b,g,r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('bred',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merge' , merged)

cv.waitKey(0)    