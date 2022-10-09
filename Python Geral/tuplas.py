# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:29:14 2022

@author: Alvaro Guilherme
"""

#%% Exercicio 72
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    valorDigitado = int(input('Digite um número entre 0 e 10\n'))
    if valorDigitado >= 0 and valorDigitado <= 10: 
        print(f'O número digitado foi {tupla[valorDigitado]}\n')
        break
    print('Tente novamente \n')
print ('Fechando...')

#%% Exercício 73
tupla73 = ('Avaí', 'Flamengo','Vasco','Palmeiras','Cruzeiro','Fluminense','Galo',
           'Fortaleza', 'Ceará', 'RB Bragantino')

# A) Apenas os 5 primeiros colocados
print(f'Os cinco primeiros colocados são: {tupla73[:5]}\n\n')
# B)
print(f'Os quatro últimos colocados são: {tupla73[6:]}\n\n')
# C) Times em ordem alfabética
print(sorted(tupla73))
# D) Qual posição está um time
time = input('Qual time deseja saber a colocação?\n')
for i in range(len(tupla73)):
    if time == tupla73[i]:
        print(f'O time do {time} está na {i+1}ª colocação\n')
        break

#%% Exercício 74
from random import sample, randint
# a = tuple(sample(range(10),5))
a = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(a)
print(f'Valor máximo: {max(a)}; Valor mínimo: {min(a)}\n')

#%% Exercício 75
tupla75 = (int(input('Digite um número\n')),int(input('Digite um número\n')),
           int(input('Digite um número\n')),int(input('Digite um número\n')))

# A)
cont1 = 0
pos = -1
pares = ''
for n2 in range(len(tupla75)):
    if tupla75[n2] == 9:
        cont1 += 1
    elif tupla75[n2] == 3 and pos < 0:
        pos = n2
    if tupla75[n2]%2 == 0:
        pares += str(tupla75[n2])+' '
        
print(f'O número 9 apareceu {cont1} vezes\n')

# B)
print(f'O primeiro 3 está na posição {pos}\n')

# C)
print(f'Números pares: {pares}')

#%% Exercício 76
# Listagem de preços
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)

# Fazendo uma forma tabular
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS"}:^40') # identado no centro
print('-'*40)
for i in range(len(listagem)):
    if i%2 == 0:
        print(f'{listagem[i]:.<30}', end='') # Enche de pontinhos até 30 caracteres
    else:
        print(f'R${listagem[i]:>7.2f}') # Identado à esquerda com duas casas decimais
print('-'*40)

#%% Exercício 77
# Contas as vogais das palavras
tupla77 = ('programar', 'python', 'java', 'computador', 'teclado')
for p in tupla77:
    print(f'\nNa palavra {p} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

















