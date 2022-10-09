import cv2 as cv 

#Captura de vídeo
cap = cv.VideoCapture(0)

#Altura e largura
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#Salvar um vídeo
writer = cv.VideoWriter("teste.mp4", cv.VideoWriter_fourcc(*"DIVX"), 20, (width, height)) #Parametros -> (nome, codec, frame, tamanho)

#Laço de repetição
while True:
	ret, frame = cap.read()
	cv.imshow("frame", frame)
	writer.write(frame)
	if cv.waitKey(1) & 0xFF == ord("q"):
		break;

cap.release()
writer.release()
cv.destroyAllWindows()