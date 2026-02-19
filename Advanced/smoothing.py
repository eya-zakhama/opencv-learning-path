import cv2 as cv


img = cv.imread('photo/girl.jpg')
cv.imshow('girl', img)





#avarging
average = cv.blur(img, (7, 7))
cv.imshow('Average Blurring', average)







cv.waitKey(0)