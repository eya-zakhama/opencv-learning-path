import cv2 as cv
import matplotlib.pyplot as plt


img =cv.imread('photo/city.jpg')
cv.imshow('city',img)

# plt.imshow(img) 
# plt.show() #display using matplotlib el color is different because matplotlib uses RGB format by default whereas OpenCV uses BGR format.


# #BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
# cv.imshow('gray', gray)



#BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)


#BGR TO LAB
rgb = cv.cvtColor(img, cv.COLOR_BGR2Lab)    
cv.imshow('RGB', rgb)


# plt.imshow(rgb)
# plt.show()


#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)


#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', hsv_bgr)




cv.waitKey(0)