# Valores principais
valor_principal1 = {}
valor_principal2 = {}
valor_principal3 = {}
# Parâmetro 1
valor_principal1['Descrição'] = 'Acesso aos Parâmetros'
valor_principal1['Faixa de Valores'] = '0 a 9999'
# Parâmetro 2
valor_principal2['Descrição'] = 'Referência Velocidade'
valor_principal2['Faixa de Valores'] = '0 a 65535'
# Parâmetro 3
valor_principal3['Descrição'] = 'Velocidade de Saída'
valor_principal3['Faixa de Valores'] = '0 a 65535'

# Dicionário
inversor = {'P0000': valor_principal1,'P0001':valor_principal2, 'P0003':valor_principal3}

#Exibindo valores
for key,value in inversor.items():
    print(key, ' -> ', value)