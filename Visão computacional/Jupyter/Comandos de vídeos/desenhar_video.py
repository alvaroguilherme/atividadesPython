import cv2 as cv 
import time

cap = cv.VideoCapture("teste.mp4")

if cap.isOpened() == False:
	print("Erro")

#RETANGULO ESTÁTICO
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# #Parte superior
# x = width // 2 #Duas barras faz a divisão ser inteira
# y = height // 2

# #Alt e lar do ret
# w = width // 4
# h = height // 4

# #Parte final x+w y+h

# while cap.isOpened():

# 	ret, frame = cap.read()

# 	cv.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255), thickness=4) 

# 	cv.imshow("frame", frame)
# 	time.sleep(1/20)
# 	if cv.waitKey(1) & 0xFF == ord("q"):
# 		break;

# cap.release()
# cv.destroyAllWindows()

#RETANGULO EM MOVIMENTO
#Callback
def draw_rect(event,x,y,flags,params):
	global pt1, pt2, topLeftClicked, bottomRightClicked
	if event == cv.EVENT_LBUTTONDOWN:
		if topLeftClicked == True and bottomRightClicked == True:
			pt1 = (0,0)
			pt2 = (0,0)
			topLeftClicked = False
			bottomRightClicked = False
		if topLeftClicked == False:
			pt1 = (x,y)
			topLeftClicked = True
		elif bottomRightClicked == False:
			pt2 = (x,y)
			bottomRightClicked = True

##Variaveis Globais
pt1 = (0, 0) #Pontos
pt2 = (0, 0)
topLeftClicked = False #Mouse
bottomRightClicked = False

cv.namedWindow("Teste")
cv.setMouseCallback("Teste", draw_rect)

while cap.isOpened():

	ret, frame = cap.read()

	##Desenhar o retangulo de acordo com as variaveis globais
	if topLeftClicked:
		cv.circle(frame, center=pt1, radius=5, color=(0,0,255))
	if topLeftClicked and bottomRightClicked:
		cv.rectangle(frame, pt1, pt2, color=(0,0,255), thickness=1)

	cv.imshow("Teste", frame)
	time.sleep(1/20)
	if cv.waitKey(1) & 0xFF == ord("q"):
		break;

cap.release()
cv.destroyAllWindows()