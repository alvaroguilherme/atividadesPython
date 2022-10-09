import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 
#notebook inline 

#EROSÃO

#Lendo imagem
img = cv.imread("placa.png")
	
# element_estr = cv.getStructuringElement(cv.MORPH_RECT, (7,7)) #Elemento estruturante -> RECT = retangular; ELLIPSE = eliptico; CROSS = cruz
# 															  #Parametros (elemento, tamanho da matriz)

# print(element_estr)

# imgProcess = cv.erode(img, element_estr, iterations=2) #Parametros -> (img, elemento estruturante, interações desejadas)

# fig = plt.figure(figsize=(10,8))
# ax1 = fig.add_subplot(211)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(212)
# plt.imshow(imgProcess)
# plt.title("Imagem processada")
# plt.show()

#DILATAÇÃO
# element_estr = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7)) #Elemento estruturante -> RECT = retangular; ELLIPSE = eliptico; CROSS = cruz
# 															  #Parametros (elemento, tamanho da matriz)

# imgDilat = cv.dilate(img, element_estr, 2) #Parametros -> (img, elemento estruturante, interações desejadas)

# fig = plt.figure(figsize=(10,8))
# ax1 = fig.add_subplot(211)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(212)
# plt.imshow(imgDilat)
# plt.title("Imagem processada")
# plt.show()

#GRADIENTE MORFOLÓGICO

#Lendo imagem
img1 = cv.imread("moeda.png")
img2 = cv.imread("esqueleto.tif")

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(121)
plt.imshow(img1)
plt.title("Imagem 1")

ax2 = fig.add_subplot(122)
plt.imshow(img2)
plt.title("Imagem 2")
plt.show()

element_estr1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
element_estr2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (21,21))

imgProc1 = cv.morphologyEx(img1, cv.MORPH_GRADIENT, element_estr1) #Parametros -> (imagem, operação que será realizada, elemento estrututral)
imgProc2 = cv.morphologyEx(img2, cv.MORPH_TOPHAT, element_estr2)
imgProc3 = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, element_estr2)

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(131)
plt.imshow(imgProc1)
plt.title("Imagem gradiente")

ax2 = fig.add_subplot(132)
plt.imshow(imgProc2)
plt.title("Imagem tophat")

ax3 = fig.add_subplot(133)
plt.imshow(imgProc3)
plt.title("Imagem blackhat")

plt.show()
