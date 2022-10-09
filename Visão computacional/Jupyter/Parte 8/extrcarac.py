import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
#notebook inline

img = cv.imread("tampa_azul.jpg", 1)
img_gray = cv.imread("tampa_azul.jpg", 0)

cv.imshow("Imagem em RGB", img)
cv.imshow("Imagem em escala de cinza", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()

valorMedio = cv.mean(img) #Retorna a média de todos os canais RGB e a transparência da imagem
valorMedioGray = cv.mean(img_gray)

(mean, std) = cv.meanStdDev(img) #Retorna a média e o desvio padrão da imagem de forma independente para cada canal do RGB
(means, stds) = cv.meanStdDev(img_gray)

#Os valores mean e std são valores escalares para imagens coloridas que dividem a imagem em canais e calculam e aplicam um limite para cada canal de forma independente

rgb = np.concatenate([mean, std]).flatten() #Retorna uma cópia da matriz em 1D
gray = np.concatenate([means, stds]).flatten()

print("Valores da média e desvio padrão RGB")
print(valorMedio)
print(rgb)

print("Valores da média e desvio padrão cinza")
print(valorMedioGray)
print(gray)