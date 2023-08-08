import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH) * 2   # float
# Get current height of frame
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
# Define Video Frame Rate in fps
fps =  15

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('lab6d_B.avi', fourcc, fps, (int(width),int(height)) )

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frameRaw = frame.copy()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)


    for i in corners:
        x,y = i.ravel()
        cv.circle(frame,(x,y),15,255,-1)
    
    # Display the resulting frame
    merge = np.concatenate((frameRaw, frame), axis = 1)
    cv.imshow('frame', merge)
    out.write(merge)    
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
