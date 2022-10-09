# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:49:38 2022

@author: Alvaro Guilherme
"""
#%% Ex 90
nome = input('Digite o nome: ')
media = float(input('Digite a média: '))
if media >= 6:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
aluno = {'nome':nome, 'media':media, 'situação':sit}
print(f'Nome é igual a {nome}')
print(f'Média é igual a {media}')
print(f'Situação é {sit}')

#%% Ex 91
from random import randint
from operator import itemgetter
from time import sleep
sorteio = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6)
           ,'jogador4':randint(1,6)}
print('Valores sorteados:')
for k,v in sorteio.items():
    print('\nJogando o dado...')
    sleep(1)
    print(f'{k} tirou o número {v}',end='\n')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print('Ranking:')
for k in ranking:
    print(k)
    
#%% Ex 92
from datetime import datetime 
dados = {}
dados['nome'] = input('Nome: ')
dados['idade'] = datetime.now().year - int(input('Data de nascimento: '))
carteira =  int(input('Possui carteira de trabalho? (1-Sim / 2-Não): '))
if carteira == 2:
    print('\nDados:')
    print(dados['nome'], end=' ')
    print(dados['idade'], 'anos')
elif carteira == 1:
    dados['dt_cont'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['dt_aposent'] = dados['dt_cont']+35
print('\nDados:')
for k,v in dados.items():
    print(f'{k} é {v}')

#%% Ex 93
jogador = {}
gols = []
jogador['nome'] = input('Qual o nome do jogador? ')
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(jogos):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
for j in range(jogos):
    print(f'   => Na partida {j+1}, fez {jogador["gols"][j]} gols')
print(f'Foi um total de {jogador["total"]} gols')

#%% Ex 94
cadastro = {}
pessoas = []
media = 0
while True:
    cadastro['nome'] = input('Nome: ')
    cadastro['sexo'] = input('Sexo: ')
    cadastro['idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    escolha = input('Deseja continuar? (S/N) ')
    if escolha.lower() == 'n':
        break
# A) Quantas pessoas foram cadastradas
print(f'\nForam cadastradas {len(pessoas)} pessoas')
# B) Média da idade
for p in pessoas:
    media += p['idade']
media /= len(pessoas)
print(f'A média de idade é de {media} anos')
# C) Lista com todas as mulheres
print('As mulheres cadastradas são',end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]};', end=' ')
# D) Lista com pessoas acima da média
print('\nAs pessoas com idades acima da média são', end=' ')
for p in pessoas:
    if p['idade']>media:
        print(f'{p["nome"]};',end=' ')
        
#%% Ex 95











