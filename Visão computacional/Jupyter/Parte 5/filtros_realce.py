import cv2 as cv
from matplotlib import pyplot as plt
#matplotlib inline

#SOBEL (REALÇAR BORDAS VERTICAIS E HORIZONTAIS)

#Lendo imagem
img = cv.imread("predio.jpg")

# imgSx = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=7) #Parametros -> (imagem, valor que representa o pixel, realce horizontal, realce vertical, dimensao da mascara)
# imgSy = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=7)

# fig = plt.figure(figsize=(20,5))
# ax1 = fig.add_subplot(131)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(132)
# plt.imshow(imgSx)
# plt.title("Imagem sobel x")

# ax3 = fig.add_subplot(133)
# plt.imshow(imgSy)
# plt.title("Imagem sobel y")
# plt.show()

#LAPLACIANO
# imgLp = cv.Laplacian(img, cv.CV_8U) #Parametros -> (imagem, valor que representa o pixel)

# fig = plt.figure(figsize=(20,5))
# ax1 = fig.add_subplot(121)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(122)
# plt.imshow(imgLp)
# plt.title("Imagem filtrada")
# plt.show()

#CANNY
imgC = cv.Canny(img, 75, 50) #Parametros -> (imagem, intensidade de detecção 1, intensidade de detecção 2)

fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(imgC, cmap=plt.cm.gray)
plt.title("Imagem filtrada")
plt.show()