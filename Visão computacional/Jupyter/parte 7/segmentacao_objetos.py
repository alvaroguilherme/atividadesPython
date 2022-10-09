import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

# #SEGMENTAÇÃO POR BINARIZAÇÃO
# #Lendo imagem
# img = cv.imread("cafe.jpg")

# metodo = cv.THRESH_BINARY_INV 
# ret, imgBin = cv.threshold(img, 200,255, metodo) #Parametros -> (imagem, limiar=valor estipulado pelo usuario, val_int=valor de intensidade dos pixels com valor maior que o limiar, metodo=(THRESH_BINARY=cor preta;THRESH_BINARY_INV=cor branca))

# fig = plt.figure(figsize=(15,15))

# ax1 = fig.add_subplot(121)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(122)
# plt.imshow(imgBin)
# plt.title("Imagem segmentada")
# plt.show()

# #BINARIZAÇÃO ADAPTATIVA
# img = cv.imread("olho.png", 0)

# #Aplicar um filtro de mediana para suaviza-la melhor
# imgGauss = cv.medianBlur(img, 7)

# th2 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5) #Parametros -> (src, intensidade max do pixel, metodo adaptativo(ADAPTIVE_THRESH_MEAN_C; ADAPTIVE_THRESH_GAUSSIAN_C), metodo, tamanho da mascara, constante de subtração da media ou meida pnderada)
# th3 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# cv.imshow("Imagem original", img)
# cv.imshow("Imagem media", th2)
# cv.imshow("Imagem gaussiana", th3)

# cv.waitKey(0)
# cv.destroyAllWindows()

#BINARIZAÇÃO POR OTSU
#Lendo imagem
img = cv.imread("cafe.jpg", 0)

metodo = cv.THRESH_BINARY_INV + cv.THRESH_OTSU
ret, imgBin = cv.threshold(img, 0, 255, metodo)
print("O melhor limiar é:", ret)

plt.hist(img.ravel(), 256, [0,256])
plt.show()
cv.imshow("Imagem original", img)
cv.imshow("Imagem otsu", imgBin)

cv.waitKey(0)
cv.destroyAllWindows