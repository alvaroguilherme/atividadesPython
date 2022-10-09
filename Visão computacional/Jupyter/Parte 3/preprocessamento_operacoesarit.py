import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

#Lendo imagens
img1 = cv.imread("Superman.png", 0)
img2 = cv.imread("batman.png", 0)

#ADIÇÃO
# imgSomada = cv.add(img1, img2)

# fig = plt.figure(figsize=(20,5))
# plt.imshow(imgSomada, cmap=plt.cm.gray)
# plt.show()

fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(1,2,1)
plt.imshow(img1, cmap=plt.cm.gray)

ax2 = fig.add_subplot(1,2,2)
plt.imshow(img2, cmap=plt.cm.gray)
plt.show()

#SUBTRAÇÃO
# imgSub = cv.subtract(img1, img2)
# fig = plt.figure(figsize=(20,5))
# plt.imshow(imgSub, cmap=plt.cm.gray)
# plt.show()

#MESCLAR
imgMesclada = cv.addWeighted(img1, 0.8, img2, 0.8, 0) #Parametros -> (src1, alpha=intensidade da 1 img, src2, beta=intensidade da 2 img, gamma)
fig = plt.figure(figsize=(20,5))
plt.imshow(imgMesclada, cmap=plt.cm.gray)
plt.show()
