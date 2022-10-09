import cv2 as cv 
import numpy as np 

img = cv.imread("estrada.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Converter para tons de cinza
edges = cv.Canny(gray, 70, 255) #Detecção de bordas por Canny

#Tranformada de Hough
lines = cv.HoughLinesP(edges, 1, np.pi/180, 10, 200) #Parametros -> (img binaria, distancia perpendicular da origem ate a linha, angulo perpendicular da linha ao eixo, comprimento min da linha, comprimento max da linha)

#Desenhar linhas detectadas
for line in lines:
	x1, y1, x2, y2 = line[0]
	cv.line(img, (x1,y1), (x2,y2), (0,255,0), 3) #Parametros -> (img binaria, coord1, coord2, cor, grossura da linha)

cv.imshow("Imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()
