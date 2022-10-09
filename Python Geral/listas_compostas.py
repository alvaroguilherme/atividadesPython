# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:19:44 2022

@author: Alvaro Guilherme
"""

#%% Ex 84
pessoas = []
lista84 = []
escolha = 's'
maior = 0
menor = 500
while escolha == 's':
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    lista84.append(pessoas[:])
    if pessoas[1] >= maior:
        maior = pessoas[1]
    if pessoas[1] <= menor:
        menor = pessoas[1]
    pessoas.clear()
    escolha = str(input('Deseja continuar? [s/n] '))
print('Qtd de pessoas cadastradas: ',len(lista84))
print(f'O maior peso foi de {maior} das pessoas: ',end='')
for p in lista84:
    if p[1] == maior:
        print(f'{p[0]} ',end='')
print(f'\nO menor peso foi de {menor} das pessoas: ',end='')
for p in lista84:
    if p[1] == menor:
        print(f'{p[0]} ',end='')
        
#%% Ex 85
lista85 = [[],[]]
for i in range(0,7):
    num = int(input('Digite um número: '))
    if num%2 == 0:
        lista85[0].append(num)
    else:
        lista85[1].append(num)
lista85[0].sort()
lista85[1].sort()
print('Valores pares: ',lista85[0])
print('\nValores ímpares: ',lista85[1])

#%% Ex 86
matriz = [[],[],[]]
cont=0
for i in range(9):
    if i != 0 and i%3 == 0:
        cont += 1
    num = int(input('Digite um número: '))
    matriz[cont].append(num)
print('-='*20)
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]} ', end='')
    print()
    
#%% Ex 87 - Utiliza os dados do exercício anterior
somaPares = 0
somaColuna3 = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j]%2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            somaColuna3 += matriz[i][j]

print('A soma dos valores pares é:',somaPares)
print('A soma dos valores da terceira coluna é:',somaColuna3)
print('O maior valor da segunda linha é:',max(matriz[1])) 

#%% Ex 88
from random import sample, randint
from time import sleep
jogos = []
lista88 = []
# jogos = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
qtd = int(input('Quantidade de jogos sorteados: '))
for i in range(qtd):
    jogos = sample(range(1,60),6)
    lista88.append(jogos[:])  
    print(f'Sorteando Jogo {i+1}')
    sleep(1) #Delay de 1 segundo
    print(lista88[i])

#%% Ex 89
alunos = []
boletim = []
escolha = 's'
media = 0
while escolha=='s':
    alunos.append(input('Digite o nome do aluno: '))
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    boletim.append(alunos[:])
    alunos.clear()
    escolha = input('Deseja continuar? [s/n]: ')
print('-='*20)
print(f'{"ID":<5}{"Nome"}{"Média":>22}')
print('-'*40)
for i in range(len(boletim)):
    for j in range(1,3):
        media += boletim[i][j]
    media /= 2
    print(f'{i+1:<5}{boletim[i][0]:<10}{media:>15.2}')
    media = 0
print('-'*40)
while True:
    c = int(input('\nDeseja saber a nota de qual aluno? (999 Interrompe): '))-1
    if c+1 == 999:
        break
    if c <= len(boletim):
        print(f'{boletim[c][0]} tirou as notas {boletim[c][1]} e {boletim[c][2]}')
    else:
        print('ID inexistente!')
    

    




















    