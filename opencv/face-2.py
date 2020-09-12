import cv2
import sys


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # kare kare webcam den gelen görüntü yakalanıyor
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, )
    #faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        #cv2.CASCADE_SCALE_IMAGE

    # Tanımalanan yüzün etrafında yeşil bir kare oluşturuluyor
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Sonuç ekranda gösteriliyor.
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# herşey tamamsa ekran yakalaması serbest bırakılıyor.
