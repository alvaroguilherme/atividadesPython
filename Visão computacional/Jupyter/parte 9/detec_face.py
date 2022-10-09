import cv2 as cv 

face_cascade = cv.CascadeClassifier('C:/projects/opencv-python/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
	ret, img = cap.read()

	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5) #Parâmetros -> (img, tamanho que ela é reduzida em cada escala da imagem, quantos vizinhos cada retangulo candidato deve ter para retê-lo)
	for (x,y,w,h) in faces:
		cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0))
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	cv.imshow("Face detectada", img)
	k = cv.waitKey(30)
	if k==27:
		break;

cap.release()
cv.destroyAllWindows()