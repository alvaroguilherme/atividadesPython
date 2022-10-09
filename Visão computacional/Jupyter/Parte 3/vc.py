import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

# #Leitura da imagem
# img = cv.imread("Cinza.jpg")

# #Mostrar imagem
# # cv.imshow("imagem", img)
# # cv.waitKey(0)
# #plt.imshow(img)


# #Mostrar histograma
# plt.hist(img.ravel(),256,[0,256])
# plt.show()

########################################
#IMAGENS COLORIDAS
#Leitura da imagem e segmentação dos canais RGB
img = cv.imread("colorida.jpg")
azul, verde, vermelho = cv.split(img)
# cv.imshow("colorida", img)
# cv.waitKey(0)

#Histogramas da imagem
fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(131) #1 linha, 3 colunas, 1ª imagem
ax1.hist(azul.ravel(),256,[0,256])
plt.title("Histograma com canal azul")

ax2 = fig.add_subplot(132) #1 linha, 3 colunas, 2ª imagem
ax2.hist(verde.ravel(),256,[0,256])
plt.title("Histograma com canal verde")

ax3 = fig.add_subplot(133) #1 linha, 3 colunas, 3ª imagem
ax3.hist(azul.ravel(),256,[0,256])
plt.title("Histograma com canal vermelho")

plt.show()