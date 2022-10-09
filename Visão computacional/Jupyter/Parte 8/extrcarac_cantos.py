#HORNIS CORNER DETECTOR
import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
#notebook inline

img = cv.imread("hospital2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# gray = np.float32(gray) #tranformando os valores dos pixels em float
# dst = cv.cornerHarris(gray, 2, 3, 0.01) #Parametros -> (imagem, tamanho dos pixels vizinhos considerados cantos, parametros de abertura de Sobel, parametro livre de Harris)
# element_estr = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
# dst = cv.dilate(dst, element_estr)

# img[dst > 0.05*dst.max()] = [0,0,255]

# fig = plt.figure(figsize=(10,8))
# plt.imshow(img)
# plt.show()

#Detecção dos melhores cantos
corners = cv.goodFeaturesToTrack(gray, 10, 0.05, 0.25) #Parâmetros -> (imagem em tons de cinza, numero de cantos que se deseja encontrar, nivel de qualidade dos cantos[entre o e 1], distancia euclidiana minima entre os cantos)

for item in corners:
	x,y = item[0]
	cv.circle(img, (x,y), 4, (0,0,255), -1)

fig = plt.figure(figsize=(10,8))
plt.imshow(img)
plt.show()
