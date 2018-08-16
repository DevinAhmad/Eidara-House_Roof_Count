import cv2
import numpy as np

rumah_cascade = cv2.CascadeClassifier('cascade_30.xml')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
gambar = 'Blok-2'
jpg = '.jpg'
img = cv2.imread(gambar+jpg, 1)
rejectLevels = 2
levelWeights = 5
scaleFactor = 0
minNeighbors = 5
flags = 0
minSize = 40
maxSize = 40
z = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
houses, numDetect = rumah_cascade.detectMultiScale2(gray, scaleFactor = 1.05 ,minNeighbors = 4)
for (x,y,w,h) in houses:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	
numDetect = len(numDetect)



print(numDetect)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, str(numDetect), (525,650), font, 1, 255)
cv2.imshow('image', img)
c = cv2.waitKey(0)
#Press F5 to save image
#cv2.imwrite(gambar+'R'+str(numDetect)+jpg, img)
cv2.destroyAllWindows()
