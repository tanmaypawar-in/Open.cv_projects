import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank' , blank)
img = cv.imread('dog.jpg')
cv.imshow('cat' , img)

# paint the image by certain color
blank[0:100] = 0,255,0  # 0,255,0 is a green color
cv.imshow('green' , blank)

# # draw a rectangle
cv.rectangle(blank, (0,0),(100,100),(0,255,0), thickness=3)
cv.imshow('rectangle', blank)

# # draw a circle
cv.circle(blank, (100,100), 30, (255,0,0), thickness=-1)
cv.imshow('circle', blank)

# # draw a line
cv.line(blank,(100,100),(200,200),(0,0,255),thickness=3)
cv.imshow('line',blank)

# write a text on img
cv.putText(blank, 'Hello, My name is Tanmay',(20,255),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,0),thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)                