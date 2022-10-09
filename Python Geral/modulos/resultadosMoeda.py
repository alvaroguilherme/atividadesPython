import moeda

valor = float(input('Valor: R$ '))
taxa = float(input('Digite em % o valor da taxa: '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,False)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor)}')
print(f'Um aumento de {taxa}% resulta em {moeda.aumentar(valor,taxa)}')
print(f'Uma redução de {taxa}% resulta em {moeda.diminuir(valor,taxa)}')