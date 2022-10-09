import cv2 as cv 
import numpy as np 

img = cv.imread("triangle.jpg", 0)

#Segmentação por binarizaçãio
tipo = cv.THRESH_BINARY_INV
_, imgBin = cv.threshold(img, 0, 255, tipo)

modo = cv.RETR_TREE
metodo = cv.CHAIN_APPROX_SIMPLE
contorno, hierarquia = cv.findContours(imgBin, modo, metodo) #Extrai de uma imagem binária os pontos que representam os contornos dos objetos segmentado

if len(contorno)>0:
	obj = contorno[0]
	area = cv.contourArea(obj)
	print(area)

	perimetro = cv.arcLength(obj, True)
	print(perimetro)
else:
	print("Sem contorno encontrado")
