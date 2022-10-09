import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

imgOriginal = cv.imread("einstein.jpg", 0)
totalLinhas, totalColunas = imgOriginal.shape
print(totalLinhas)
print(totalColunas)

#ROTAÇÃO
# mat = cv.getRotationMatrix2D((totalLinhas/2, totalColunas/2), 45, 1) #Parametros -> (centro,angulo,escala(default=1))

# imgRotacionada = cv.warpAffine(imgOriginal, mat, (totalLinhas, totalColunas)) #Parametros -> (src, matriz de rotação, dsize)

# fig = plt.figure(figsize=(10,8))
# cv.imshow("Rotacionada", imgRotacionada)
# cv.waitKey(0)

#TRANSLAÇÃO
# matriz = np.float32([[1,0,100], [0,1,100]]) #Parametros -> ([horizontal, vertical, qtd de pixels de deslocamento])
# imgDeslocada = cv.warpAffine(imgOriginal, matriz, (totalLinhas, totalColunas))
# fig = plt.figure(figsize=(10,8))
# plt.imshow(imgDeslocada, cmap=plt.cm.gray)
# plt.show()

#ESCALA
imgModificada = cv.resize(imgOriginal, None, fx = 0.8, fy = 0.8, interpolation=cv.INTER_CUBIC) #Parametros -> (src, dst=imagem de saída, fx = fator de escala horizontal, fy = vertical, interpolation=metodo de interpolação)

cv.imshow("Original", imgOriginal)
cv.imshow("Modificada", imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()