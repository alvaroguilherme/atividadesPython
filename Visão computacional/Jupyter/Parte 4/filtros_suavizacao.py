import cv2 as cv
from matplotlib import pyplot as plt
#matplotlib inline

#FILTRO MÉDIA

#Lendo imagem
# img = cv.imread("einstein.png")

# imgM = cv.blur(img, (5,5)) #Parametros -> (imagem, máscara=dimensão da mascara=usar valores ímpares)
# fig = plt.figure(figsize=(20,5))
# ax1 = fig.add_subplot(121)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(122)
# plt.imshow(imgM)
# plt.title("Imagem filtrada")
# plt.show()

#FILTRO GAUSSIANO

#Lendo imagem
# img = cv.imread("formas.png")

# imgG = cv.GaussianBlur(img, (7,7), 0) #Parametros -> (imagem, mascara, grau de suavização)
# fig = plt.figure(figsize=(20,5))
# ax1 = fig.add_subplot(121)
# plt.imshow(img)
# plt.title("Imagem original")

# ax2 = fig.add_subplot(122)
# plt.imshow(imgG)
# plt.title("Imagem filtrada")
# plt.show()

#FILTRO MEDIANO (sal e pimenta)

#Lendo imagem
img = cv.imread("head.png")

imgMed = cv.medianBlur(img, 5) #Parametros -> (imagem, grau de suavização)
fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(imgMed)
plt.title("Imagem filtrada")
plt.show()