# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:58:14 2022

@author: Alvaro Guilherme
"""

#%% Ex 9
prescritos = 'ab'
estoque = 'ab'
qtd = 0
for med in prescritos:
    if med in estoque:
        qtd += 1
        estoque = estoque.replace(med,"")
if qtd == len(prescritos):
    saida=True
else:
    saida=False
print(saida)

#%% Ex 10
from matplotlib import pyplot as plt

datas = ['2020-07-10','2021-05-10','2021-05-10','2022-01-10','2022-01-10','2022-02-21',
         '2019-06-12','2022-04-03','2021-10-12','2022-04-03','2022-01-01','2022-01-10']
datas.sort() # Deixando as datas em ordem crescente
datasSeparadas = [] # Separando as datas sem levar em conta as repetições

qtdAtend = 1
qtdAtendGraf = [] # quantidade de atendimentos de cada data, seguindo as posições
                  # da lista de datasSeparadas
                  
for i in range(len(datas)):
    if i < len(datas)-1:
          if(datas[i]==datas[i+1]): # Comparando a data com a próxima posição, já que estão em ordem crescente
              qtdAtend += 1 
          else:
              datasSeparadas.append(datas[i])
              qtdAtendGraf.append(qtdAtend)
              qtdAtend = 1
    else:
        datasSeparadas.append(datas[i])
        qtdAtendGraf.append(qtdAtend)          

# Largura da barra
barwidth = 0.2
# Layout do gráfico
fig,ax = plt.subplots(figsize=(10,3.5))
ax.bar(datasSeparadas,qtdAtendGraf, width=barwidth)
ax.grid()
ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")
ax.grid(which="minor", ls='-.', lw=0.5)
ax.set_ylabel('Quantidade de atendimentos' ,labelpad=8)
ax.set_xlabel('Data' ,labelpad=8)
plt.show()















