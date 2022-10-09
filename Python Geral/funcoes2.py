# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:28:43 2022

@author: Alvaro Guilherme
"""

#%% Ex 101
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        print(f'Com {idade} anos. Não Vota')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos. Voto obrigatório')
    else:
        print(f'Com {idade} anos. Voto opcional')
        
        
voto(int(input('Digite o ano de nascimento: ')))

#%% Ex 102
def fatorial(num,show=False):
    f = 1
    for i in range(num,0,-1):
        f *= i
        if show:
            if i > 1:
                print(f'{i}*', end='')
            else:
                print(f'{i} =',end=' ')
    print(f)
    

fatorial(int(input('Digite um número para o cálculo do fatorial: ')), True)

#%% Ex 103
def jogador(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s)')


nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome,gols)
    
#%% Ex 104
def leiaInt(inp):
    carac = input(inp)
    if carac.isnumeric():
        carac = int(carac)
        print('O valor digitado foi',carac)
        return True
    else:
        print('\033[0;31mERRO! Digite um número inteiro\033[m')
        return False


while True:
    if leiaInt('Digite um número: '):
        break

#%% Ex 105
def notas(*nota, sit=False):
    """
    Nota: notas dos alunos
    Sit (Opcional): Situação em relação à média das notas
    """
    media = 0
    dicNotas = {}
    dicNotas['qtd'] = len(nota)
    dicNotas['maior'] = max(nota)
    dicNotas['menor'] = min(nota)
    for m in nota:
        media += m
    dicNotas['média'] = media/len(nota)
    if sit:
        if dicNotas['média'] < 6:
            dicNotas['sit'] = 'RUIM'
        elif dicNotas['média'] >= 6 and dicNotas['média'] < 7:
            dicNotas['sit'] = 'RAZOAVEL'
        else:
            dicNotas['sit'] = 'BOA'
    print(dicNotas)
    

notas(5,6,6,10,sit=True)

#%% Ex 106
def ajuda(func):
    from time import sleep
    sleep(2)
    print('\033[1;7;44m~\033[m'*50)
    print(f'\033[1;7;44m{"Acessando o manual do comando":^40}\033[m',end='')
    print(f'\033[1;3;44m{func:<10}\033[m')
    print('\033[1;7;44m~\033[m'*50)
    sleep(2)
    print(f'\033[7;30{help(func)}\033[m')
    

print('\033[1;7;45m~\033[m'*50)
print(f'\033[1;7;45m{"SISTEMA DE AJUDA":^50}\033[m')
print('\033[1;7;45m~\033[m'*50)
ajuda(input('Função: '))









