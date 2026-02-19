import cv2 as cv



#reading images
#img = cv.imread('photo/big cat.jpg')
#cv.imshow('dog',img)

#reading videos
capture = cv.VideoCapture('videos/video.mp4')
while True :
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF == ord('d') :
        break

capture.release()
cv.destroyAllWindows()
