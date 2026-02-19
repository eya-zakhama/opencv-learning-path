import cv2 as cv
import numpy as np

img=cv.imread('photo/dog.jpg')
cv.imshow('dog',img) 

#translation (moving an image (or parts of it) across a plane without changing size/shape)
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #transformation matrix 
    #to get the rotation we need to change the 2nd row 2nd column to 1
    #whe should get 2 equation like this: x_new = x_old + x and y_new = y_old + y
    #soo that's why we have 1,0,x and 0,1,y
    dimensions = (img.shape[1], img.shape[0]) #img.shape[]is tuple
    #shape[1] is width, shape[0] is height
    return cv.warpAffine(img, transMat, dimensions)
#warpAffine applies the transformation matrix to every pixel and generates the shifted image.
# -x --> left
# -y --> up 
# +x --> right
# +y --> down
translated = translate(img,-100,100)
cv.imshow('translated', translated)


#rotation
def rotate(img, angle, rotPoint=None):#rotPoint is rotation point
    (height, width) = img.shape[:2] #we didn't use shape[2] because it's number of channels and we need only height and width

    if rotPoint is None:
        rotPoint = (width//2, height//2) #center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)   
    #1.0 is scale factor (1.0 means no scaling)  >1 → zoom in , <1 → zoom out
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45) #rotate 45 degrees around center
cv.imshow('rotated', rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#interpolation methods: INTER_CUBIC, INTER_LINEAR, INTER_AREA

#flipping
flipped = cv.flip(img,0) #0->vertical, 1->horizontal, -1->both
cv.imshow('flipped', flipped)


#cropping
cropped = img[100:200, 200:300] #img[y1:y2, x1:x2]
cv.imshow('cropped', cropped)

cv.waitKey(0)
