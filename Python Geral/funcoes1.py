# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:44:07 2022

@author: Alvaro Guilherme
"""

#%% Ex 96
def area(larg, comp):
    area = larg*comp
    print(f'O terreno de {larg}x{comp} possui área igual a {area}m²')
    

area(4,6)

#%% Ex 97
def escreva(msg):
    print('~'*(len(msg)+3))
    print(f'{msg:^{len(msg)+3}}')
    print('~'*(len(msg)+3))
    
    
escreva('Olá mundo!')

#%% Ex 98
from time import sleep
def contador():
    print('-='*20)
    print('Contando de 1 até 10, de 1 em 1')
    print('-='*20)
    for i in range(1,11):
        print(i, end=' ', flush=True)
        sleep(0.25)
    print()
    print('-='*20)
    print('Contando de 10 até 0, de 2 em 2')
    print('-='*20)
    j = 10
    while j>=0:
        print(j, end=' ', flush=True)
        j -= 2
        sleep(0.25)
    print()
    print('-='*20)
    print('Contagem personalizada')
    print('-='*20)
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: ')) 
    num = inicio
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    if inicio < fim:
        while num <= fim:
            print(num, end=' ', flush=True)
            num += passo
            sleep(0.25)
    elif inicio > fim:
        while num >= fim:
            print(num, end=' ', flush=True)
            num -= passo
            sleep(0.25)
    else:
        print('Valores são iguais!')
        
             
contador()

#%% Ex 99
def maior(*numeros):
    print('-='*20)
    print(numeros)
    print(f'Foram informados {len(numeros)} valores')
    print(f'O maior valor informado foi {max(numeros)}')
    print('-='*20)
    

maior(2,5,6,7,3,10)
maior(7,-2)
maior(5,12,3,5)

#%% Ex 100
from random import randint
def sorteio():
    lista100 = []
    for i in range(5):
        lista100.append(randint(1,10))
    print('-='*20)
    print('Números sorteados: ',lista100)
    return lista100

def somaPar(lista):
    soma = 0
    for v in lista:
        if v%2 == 0:
            soma += v
    print('Soma dos números pares é:',soma)
    print('-='*20)


somaPar(sorteio())













    