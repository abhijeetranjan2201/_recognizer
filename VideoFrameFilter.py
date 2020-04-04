import cv2
import sys

faceCascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture('vid.mp4')
increment = 0  #---Declare a variable that will increment for every image saved
while True:
# Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=2.0, minNeighbors=5)

# Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
    cv2.imshow('Video', frame)
    increment = increment + 1  #--- Initiate the increment variable
    if cv2.waitKey(1) & 0xFF == ord('q'):
    # Write frame in file
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)        
            cv2.imwrite('only_face' + str(increment) + '.jpg')  #--- Here is where the increment variable is placed. It will be incremented for every face and thus saving every face that gets detected.
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()