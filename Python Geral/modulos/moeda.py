# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:00:41 2022

@author: Alvaro Guilherme
"""

def dobro(num,formatar=True):
    if formatar:
        return moeda(num*2)
    else:
        return num*2


def metade(num,formatar=True):
    if formatar:
        return moeda(num/2)
    else:
        return num/2


def aumentar(num,taxa,formatar=True):
    taxa += 100
    taxa /= 100
    if formatar:
        return moeda(num*taxa)
    else:
        return num*taxa


def diminuir(num,taxa,formatar=True):
    taxa -= 100
    taxa /= 100
    if formatar:
        return moeda(num*taxa*-1)
    else:
        return num*taxa*-1


def moeda(num):
    return f'R$ {num}'











