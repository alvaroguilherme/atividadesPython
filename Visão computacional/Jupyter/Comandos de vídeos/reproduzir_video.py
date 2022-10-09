import cv2 as cv 
import time

cap = cv.VideoCapture("teste.mp4")

if cap.isOpened() == False:
	print("Erro")

while cap.isOpened():
	ret, frame = cap.read()

	if(ret == True):
		cv.imshow("frame", frame)
		time.sleep(1/20) #dividir pelo numero de frames
		if(cv.waitKey(1) & 0xFF == ord("q")):
			break;
	else:
		break;

cap.release()
cv.destroyAllWindows()
