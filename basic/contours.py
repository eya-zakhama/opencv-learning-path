import cv2 as cv
import numpy as np

img =cv.imread('photo/dog.jpg')
cv.imshow('dog',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) 

#cv.imshow('thresh', thresh)#tchouf taswira noir et blanche




contours , hierarchies = cv.findContours(canny, 
                                         cv.RETR_LIST,
                                         cv.CHAIN_APPROX_SIMPLE
                                         )     #cv.RETR_EXTERNAL retrieves only the extreme outer contours.you can use other modes like cv.RETR_LIST (full hierarchy), cv.RETR_CCOMP(all contours), cv.RETR_TREE(two-level hierarchy) based on your needs.
#cv.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangle is encoded with 4 points.(Removes unnecessary points + Keeps only key points)

print(f'Total contours found: {len(contours)}')


#will draw all contours on the blank image
cv.drawContours(blank, contours, -1, (0,255,0), 1) #-1 means draw all contours 
#cv.drawContours(img, contours, max_contour_index, color, thickness)
cv.imshow('contours drawn', blank)


cv.waitKey(0)