import cv2 as cv

#img = cv.imread('photo/big cat.jpg')
#cv.imshow('dog',img)

def rescaleFrame (frame, scale=0.75):
    #images, videos and live video
    widh = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )
    dimentions =(widh,height)
    return cv.resize(frame, dimentions , interpolation =cv.INTER_AREA)


def changeRES(width, height):
    #live video
    capture.set(3, width)
    capture.set(4, height )
    
    
    
capture = cv.VideoCapture('videos/video.mp4')
while True :
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('videp resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d') : 
        
        break


cv.waitKey(0)