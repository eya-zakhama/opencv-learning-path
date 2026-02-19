import cv2 as cv
import numpy as np


img =cv.imread('photo/girl.jpg')
cv.imshow('girl',img)

blank = np.zeros(img.shape[:2], dtype='uint8') #img.shape[:2] → (height, width)


b,g,r = cv.split(img)
#Rebuild images with ONE color channel
#cv.merge():
#Takes three single-channel images
#Combines them into a 3-channel color image
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('blue', blue) # display blue channel
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape) #(height, width, channels) channels =3 for BGR
print(b.shape)  # (height, width)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)


