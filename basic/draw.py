import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #zeros() → creates an array filled with zeros 
#cv.imshow('blank', blank)

img = cv.imread('photo\\dog.jpg')
cv.imshow('dog',img)





#1. point the image certain color
blank[200:300, 200:300] = 0,0,255 #200:300, 200:300 is the area to color
cv.imshow('red', blank)


#2. draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED) #cv.FILLED or -1 fills the rectangle
#cv.rectangle(image, pt1, pt2, color, thickness)  
cv.imshow('rectangle', blank)




#3. draw a circle
cv.circle(blank, (250,250), 40, (255,0,0), thickness=-1) 
#cv.circle(image, center, radius, color, thickness)
cv.imshow('circle', blank)



#4. draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)



#cv.line(image, pt1, pt2, color, thickness)
cv.imshow('line', blank)
cv.waitKey(0)



#5. write text
cv.putText(blank, 'Hello World', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255),2) 


#cv.putText(image, text, org, fontFace, fontScale, color, thickness)
cv.imshow('text', blank)
cv.waitKey(0)