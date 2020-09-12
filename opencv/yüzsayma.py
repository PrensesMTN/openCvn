import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
while(True):
    ret, img = capture.read()
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage)
    print(type(faces))
    if len(faces) == 0:
        cv2.putText(img, "yuzler: 0" , (0, img.shape[0] - 10),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0 , 255), 1)
        cv2.rectangle(img, ((0, img.shape[0] - 25)), (270, img.shape[0]), (255, 0, 250 ), -1)
        cv2.putText(img, "yuzler: " + str(faces.shape[0]), (0, img.shape[0] - 10),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 10, 0), 1)
        cv2.imshow('Image with faces', img)
        #if (cv2.waitKey(1) == 27):
       #     break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
