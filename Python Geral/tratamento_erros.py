# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:49:26 2022

@author: Alvaro Guilherme
"""

#%% Ex 113
def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário não digitou um valor!\033[m')
            return 0
            break
        # except Exception as erro:
        #     print(erro.__class__)
        else:
            return num
            break
    

def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário não digitou um valor!\033[m')
            return 0
            break
        # except Exception as erro:
        #     print(erro.__class__)
        else:
            return num
            break
    

a = leiaInt()
b = leiaFloat()
print(f'Números digitados: Inteiro: {a}, Real: {b}')

#%% Ex 114
# Erro para acessar sites
import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível')
else:
    print('Acessado!')





















