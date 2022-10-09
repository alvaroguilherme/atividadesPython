import matplotlib.pyplot as plt
#Visualização de dados em Python

#PLOTAR GRÁFICOS
# x = [1,2,3,4,5]
# y = [2,3,7,1,9]
# titulo = "Gráfico"
# eixox = "Eixo x"
# eixoy  ="Eixo y"

# #Legendas
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)

# #plt.plot(x,y) #Gráfico de linha
# plt.bar(x,y) #Gráfico de barra
# plt.show()

###############################################
#COMPARAÇÃO DE GRÁFICOS
# x1 = [1,3,5,7,9]
# y1 = [2,6,4,1,3]

# x2 = [2,4,6,8,10]
# y2 = [5,1,3,7,9]

# z = [100,30,200,150,85]

# #titulo = "Gráfico de barras 2"
# titulo = "Scatterplot: Gráfico de dispersão"
# eixox = "Eixo x"
# eixoy = "Eixo y"

# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)

# # plt.bar(x1,y1,label = "Grupo 1")
# # plt.bar(x2,y2,label = "Grupo 2")
# plt.scatter(x1,y1, label = "Pontos", color = "r", marker = "h", s = z) #Pontos #s = size | color = "#876510" Intensidade do RGB
# plt.plot(x1,y1, label = "Linhas", color = "k", linestyle = ":") #Linhas
# plt.legend()

# #plt.show() #Mostra o gráfico
# plt.savefig("Figura1.png", dpi = 72) #Salva a imagem do gráfico | Impressao dpi=300; Monitor dpi=72

################################################################################
#ESTUDO DE CASOS - CRESCIMENTO DA POPULAÇÃO BRASILEIRA
dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0: #ignora a primeira linha
		linha = dados[i].split(";")
		x.append(int(linha[0])) #Dados antes do ;
		y.append(int(linha[1])) #Dados depois do ;

print(x) #Anos
print(y) #Tamanho população

#Gráfico dos dados
titulo = "Crescimento da população brasileira 1980-2016"
eixox = "População x100 milhões"
eixoy = "Ano"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y, color = "#e4e4e4")
plt.plot(x,y, color = "k", linestyle = "--")

plt.show()


################################################################################
# color: cor (ver exemplos abaixo)

# label: rótulo

# linestyle: estilo de linha (ver exemplos abaixo)

# linewidth: largura da linha

# marker: marcador (ver exemplos abaixo)



# CORES (color)
# 'b' blue

# 'g' green

# 'r' red

# 'c' cyan

# 'm' magenta

# 'y' yellow

# 'k' black

# 'w' white



# Marcadores (marker)
# '.' point marker

# ',' pixel marker

# 'o' circle marker

# 'v' triangle_down marker

# '^' triangle_up marker

# '<' triangle_left marker

# '>' triangle_right marker

# '1' tri_down marker

# '2' tri_up marker

# '3' tri_left marker

# '4' tri_right marker

# 's' square marker

# 'p' pentagon marker

# '*' star marker

# 'h' hexagon1 marker

# 'H' hexagon2 marker

# '+' plus marker

# 'x' x marker

# 'D' diamond marker

# 'd' thin_diamond marker

# '|' vline marker

# '_' hline marker





# Tipos de linha (linestyle)
# '-' solid line style

# '--' dashed line style

# '-.' dash-dot line style

# ':' dotted line style

