import cv2
import numpy as np

filename = 'images.jfif'
img = cv2.imread(filename)
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gri = np.float32(gri)
dst = cv2.cornerHarris(gri,2,3,0.04)

#köşeleri işaretlemek için , genişletme yapıldı.
dst = cv2.dilate(dst,None)

# eşik değer görüntüye bağlı olarak değiebilir
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
