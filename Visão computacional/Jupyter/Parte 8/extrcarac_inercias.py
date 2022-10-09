import cv2 as cv 

img = cv.imread("circle.jpg", 0)

#Momentos de um imagem
momentos = cv.moments(img)

# print(len(momentos))
# print(momentos)

# area = momentos['m00'] #area

# #médias
# x = momentos['m10']/area
# y = momentos['m01']/area

# #centroide
# cx = int(momentos['m10']/area)
# cy = int(momentos['m01']/area)

#Momentos invariante de Hu
import numpy as np 

momentosHu = cv.HuMoments(momentos)
print(momentosHu.flatten())

