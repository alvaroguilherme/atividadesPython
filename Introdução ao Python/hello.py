# -*- coding: utf-8 -*-
# print("Hello world!")
# # Comentário

# print("Olá mundo!")
# """
# comentário
# múltiplas 
# linhas
# """ 

# ##############################################
# print(2**3) #Exponencial (2 elevado a 3)
# print(10%3) #Resto

# ##############################################
# x = 2
# y = 3
# z = 2
# print(x<y)
# print(x==y)
# print(x<y and y==z)
# print(x==y or x==z)

# #############################################
# if x==y:
# 	print("números iguais")
# elif x<y:
# 	print("x é menor que y")
# elif y>x:
# 	print("y é maior que x")
# else:
# 	print("números diferentes")
# x += 1
# print(x)

############################################
# vetor = [1,2,3,4,5]
# for i in vetor:
# 	print(i) 
# for i in range(10,20,2):
# 	print(i)

# ############################################
# var1 = "Olá"
# var2 = "mundo!"
# concatenacao = var1 + " " + var2 + "\n"
# print(concatenacao)
# tamanho = len(concatenacao) # Lenght; conta o espaço 
# print(tamanho)
# print(var1[2]) # Caractere da posição
# print(concatenacao[0:3]) # Imprime o intervalo da sentença
# print(concatenacao)
# print(concatenacao.lower()) # Maiúsculo
# print(concatenacao.upper()) # Minúsculo
# print(concatenacao.strip()) # Retira espaços e/ou caracteres especiais no início e fim da string

# var3 = "A flor da noite da boate azul"
# vetor2 =  var3.split() # Separa as palavras em diferentes posições de um vetor
# print(vetor2)
# vetor2 = var3.split("o") # Faz a quebra onde está a letra do parâmetro
# print(vetor2)
# busca = var3.find("boate") # Localiza a posição da string do parâmetro
# print(busca)
# mudar = var3.replace("azul", "vermelha") # Altera um elemento da string
# print(mudar)

# #############################################
# def soma(x,y):
# 	return x+y
# s = soma(2,3)
# print(s)

# def mult(x,y):
# 	return x*y
# m = mult(2,3)
# print(m)

# print(soma(s,m))

# #############################################
# arquivo = open("arquivo.txt") #lê um arquivo existente
# print(arquivo)

# # linhas = arquivo.readlines()
# # print(linhas)
# # for linha in linhas:
# # 	print(linha)

# texto_completo = arquivo.read()
# print(texto_completo)

# w = open("arquivo2.txt", "w") #cria um arquivo para escrita
# w.write("Este é o meu arquivo") #escreve no arquivo
# w.close() #fecha o arquivo

# a = open("arquivo.txt", "a") #abre o arquivo para escrita e leitura (não apaga o conteúdo do arquivo para adicionar)
# a.write("Este é o meu arquivo\n") #escreve no arquivo
# a.close() #fecha o arquivo

# #############################################
# minha_lista = ["abacaxi", "melancia", "laranja"] #lista de strings
# minha_lista2 = [1,2,3,4,5] #lista de inteiros
# minha_lista3 = ["morango", 9.89, 3] #lista mista

# print(minha_lista)
# print(minha_lista2)
# print(minha_lista3)

# tamanho = len(minha_lista) #tamanho do vetor
# print(tamanho)
# print(minha_lista2[0]) #printa elemento da posição 1

# minha_lista.append("limão") #adiciona valor à lista
# print(minha_lista)

# if 7 in minha_lista2:
# 	print("7 está na lista")
# elif 3 in minha_lista2:
# 	print("3 está na lista")
# else:
# 	print("Não há 3 e 7 na lista")

# del minha_lista[2:] #remove do item 2 até o final
# print(minha_lista)
# del minha_lista3[:] #remove todas as linhas
# print(minha_lista3)

# lista = [13,767,1,4,98,4,2,468,567,34,42,7]
# lista.reverse() #inverte a lista
# print(lista)
# sorted(lista) #retorna a lista ordenada mas não muda a lista
# print(lista)
# lista.sort() #ordena a lista
# print(lista)
# lista.sort(reverse=True) #ordena decrescente
# print(lista)

# lista2 = ["bola", "azul", "campo"]
# lista2.sort() #ordena em ordem alfabética
# print(lista2)
# lista2.sort(reverse=True) #ordena decrescente
# print(lista2)

# #############################################
# meu_dicionario = {"Google":"google.com", "Facebook":"facebook.com"}
# print(meu_dicionario["Google"])
# print(meu_dicionario["Facebook"])
# print(meu_dicionario)

# for chave in meu_dicionario:
# 	print(chave)
# 	print(meu_dicionario[chave])

# for i in meu_dicionario.items():
# 	print(i)
# for i in meu_dicionario.values():
# 	print(i)
# for i in meu_dicionario.keys():
# 	print(i)

# #############################################
# import random

# num = random.randint(0,10) #escolhe um número inteiro aleatório entre 0 e 10
# print(num)

# lista = [6,45,9,7,5,3]
# num = random.choice(lista) #escolhe um número aleatório que está na lista
# print(num)

# #############################################
# #EXCEÇÃO
# a = 2
# b = 0

# try:
# 	print(a/b)
# except:
# 	print("Não é permitida a divisão por 0") #não para a execução do programa

# print (a+b)

# #############################################
# #LIST COMPREHENSION
# x = [1,2,3,4,5]
# y = []
# #z = [valor_a_adicionar laço condição]

# for i in x:
# 	y.append(i**2) #eleva cada numero da lista ao quadrado
# print(y)

# z = [i**2 for i in x] #sem condição nesse caso
# print(z)

# w = [i for i in x if i%2==1] #recebe só os impares
# print(w)

# #############################################
# #ENUMERATE
# lista = ["abacate", "melancia", "ameixa"]
# for i in range(len(lista)):
# 	print(i, lista[i])

# for i, nome in enumerate(lista):
# 	print(i, nome)

# #############################################
# #MAP
# def dobro(x):
# 	return x*2
# valor = [1,2,3,4,5]
# print(dobro(valor)) #esta dobrando a lista e nao os numeros

# print(map(dobro, valor)) #retorna apenas o endereço

# valor_dobrado = map(dobro, valor)
# # for v in valor_dobrado:
# # 	print(v)
# #ou
# valor_dobrado = list(valor_dobrado) #transforma em lista
# print(valor_dobrado)

# #############################################
# #REDUCE
# from functools import reduce
# def soma(x,y):
# 	return x+y
# lista = [1,3,5,7,9,11]

# somar = reduce(soma, lista) #soma todos os elementos da lista
# print(somar)

# #############################################
# #ZIP
# lista1 = [1,2,3,4,5]
# lista2 = ["a", "b", "c", "d", "e"]

# for numero, letra in zip(lista1, lista2):
# 	print(numero, letra) #concatena as duas listas

#############################################
#FILTER
def pares(x):
	if x%2==0:
		return x
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = filter(pares, lista1)
print(list(lista2))




