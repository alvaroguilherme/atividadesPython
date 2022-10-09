# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:46:33 2022

@author: Alvaro Guilherme
"""

#%% Ex 78
lista78 = []
for i in range(0,5):
    lista78.append(int(input('Digite um número:\n')))
for l,v in enumerate(lista78):
    if v==max(lista78):
        posMax = l
        print("\nMáximo:",max(lista78)," na posição",posMax)
    elif v==min(lista78):
        posMin = l
        print("\nMínimo:",min(lista78)," na posição",posMin)
        
#%% Ex 79
lista79 = []
while True:
    print('-'*20)
    print('1 - Digitar um novo valor\n')
    print('2 - Exibir valores')
    print('-'*20)
    escolha = int(input(''))
    if escolha == 1:
        valor = int(input('Digite o valor:\n'))
        if valor not in lista79:
            lista79.append(valor)
    if escolha == 2:
        lista79.sort()
        print(lista79)
        break

#%% Ex 80
lista80 = []
for i in range(0,5):
    aux = 0
    valor = int(input('Digite um valor:\n'))
    for l,v in enumerate(lista80):
        if valor < v and aux == 0:
            lista80.insert(l,valor)
            aux += 1
    if aux == 0:
        lista80.append(valor)
print(lista80)

#%% Ex 81
lista81 = []
while True:
    print('-'*20)
    print('1 - Digitar um valor')
    print('2 - Exibir resultados')
    print('-'*20)
    escolha = int(input(''))
    if escolha == 1:
        valor = int(input('Digite um número:\n'))
        lista81.append(valor)
    if escolha == 2:
        print(f'Foram digitados {len(lista81)} números')
        lista81.sort(reverse=True)
        print(lista81)
        if 5 in lista81:
            print('O número 5 está na lista')
        else:
            print('O número não 5 está na lista')
        break
    
#%% Ex 82
lista82 = []
listapar = []
listaimpar = []
while True:
    print('-'*20)
    print('1 - Digitar um valor')
    print('2 - Exibir resultados')
    print('-'*20)
    escolha = int(input(''))
    if escolha == 1:
        valor = int(input('Digite um número:\n'))
        lista82.append(valor)
    if escolha == 2:
        for v in lista82:
            if v%2 == 0:
                listapar.append(v)
            else:
                listaimpar.append(v)
        print(lista82)
        print(listapar)
        print(listaimpar)
        break
    
#%% Ex 83
expressao = input('Digite uma expressão:\n')
lista83 = list(expressao)
pa = pf = 0
for p in lista83:
    if p == '(':
        pa += 1
    elif p == ')':
        pf += 1
if pa == pf:
    print('Expressão está correta!')
else:
    print('Expressão incorreta!')









