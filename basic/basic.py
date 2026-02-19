import cv2 as cv

img= cv.imread('photo/1007.jpg')

cv.imshow('dog', img)


#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
#cv.COLOR_BGR2GRAY is used to convert BGR image to Grayscale
#cv.imshow('gray', gray)




#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) 
#cv.BORDER_DEFAULT is used to apply the default border type
#(7,7) is the kernel size hwa matrix size yt7kem fi blurring ( CNN)

#cv.imshow('blur', blur)



#edge cascade
##It looks at the image and draws the outlines of objects (like borders, shapes, contours).
canny = cv.Canny(img, 125, 175) #Canny edge detection algorithm. 
#The two values (125 and 175) are thresholds for edge detection.
cv.imshow('canny', canny)
# how two values effect the image:
#Numbers are LOW (example: 50, 100) → I see edges EVERYWHERE
#Numbers are HIGH (example: 200, 250) → STRONGEST edges
#Numbers are balanced (example: 125, 175) → JUST RIGHT edges
#canny = cv.Canny(blur, 125, 175) # you can also apply canny on blurred image




#dilate the image
dilated = cv.dilate(canny, (3,3), iterations=1) 
#cv.dilate() makes the white areas in an image more prominent(tzid fi la5tout).
#(3,3) is the kernel size used for dilation.
#iterations=1 means the dilation process is applied once.
cv.imshow('dilated', dilated)


#Eroding 
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.erode() shrinks the white areas in an image.(na9sou minou)  
#we apply this fonction on the dilated image to be come back to the original image after dilation.
cv.imshow('eroded', eroded)

#resize
rezised = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#interpolation=cv.INTER_AREA is used to resample the image
# INTER_AREA is best when you make an image smaller.
#cv.INTER_LINEAR is good for zooming.
# INTER_CUBIC is also good for zooming, but slower than INTER_LINEAR.
#cv.resize(image, (width, height))
cv.imshow('rezised', rezised)



#cropping
cropped = img[50:200, 200:400]
#img[y1:y2, x1:x2]
cv.imshow('cropped', cropped)

cv.waitKey(0)