import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

#Lendo imagem
img = cv.imread("einstein.jpg", 0) #parâmetros - 0 = tons de cinza; 1 = colorida; -1 = canal alfa

#Equalizar imagem
imgEqualizada = cv.equalizeHist(img)

fig = plt.figure(figsize=(20,5)) #tamanho da imagem
ax1 = fig.add_subplot(221)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(222)
plt.imshow(imgEqualizada, cmap=plt.cm.gray)

#Histogramas
ax3 = fig.add_subplot(223)
plt.hist(img.ravel(), 256, [0,256])

ax4 = fig.add_subplot(224)
plt.hist(imgEqualizada.ravel(), 256, [0,256])

plt.show()