import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
#matplotlib inline

full = cv.imread("ex_template_matching.jpg")
full = cv.cvtColor(full, cv.COLOR_BGR2RGB)
plt.imshow(full)
plt.show()

#subimagem para comparação
face = cv.imread("rosto_template.jpg")
face = cv.cvtColor(face, cv.COLOR_BGR2RGB)
plt.imshow(face)
plt.show()

#Alt, lar e canal do template matching
height, width, channels = face.shape
#Todos os 6 métodos de comparação em uma lista
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# for m in methods:
# 	#criar uma cópia da imagem
# 	full_copy = full.copy()
# 	#Eval converte uma string em uma função
# 	method = eval(m)
# 	#Aplicar TM com os métodos
# 	res = cv.matchTemplate(full_copy, face, method)

# 	plt.imshow(res)
# 	plt.title(m)
# 	plt.show()


for m in methods:
	#criar uma cópia da imagem
	full_copy = full.copy()

	#Eval converte uma string em uma função
	method = eval(m)

	#Aplicar TM com os métodos
	res = cv.matchTemplate(full_copy, face, method)

	#pegar os valores max e min além de seus locais
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

	#configurar o retangulo
	#se o método for SQDIFF pegar o min
	if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc

	bottom_right = (top_left[0] + width, top_left[1] + height)

	cv.rectangle(full_copy, top_left, bottom_right, 255, 10)

	plt.subplot(121)
	plt.imshow(res)
	plt.title("Resultado do template matching")
	plt.subplot(122)
	plt.imshow(full_copy)
	plt.title("Pontos correlacionados")
	plt.suptitle(m)

	plt.show()
	print("\n")
	
