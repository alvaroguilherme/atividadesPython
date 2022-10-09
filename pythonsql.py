# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:48:12 2022

@author: Alvaro Guilherme
"""

import csv
import mysql.connector
from mysql.connector import Error

#%% Excel
# f = open('teste.csv','w',newline='',encoding='utf-8')
# w = csv.writer(f)
# for i in range(5):
#   w.writerow([i, i*2, i*3])
with open('teste.csv',mode='r') as arq:
    arq_csv = csv.reader(arq, delimiter=',')
    for i, linha in enumerate(arq):
        print(linha)   
        try:
            conexao = mysql.connector.connect(host='localhost', database='estagio',user='root'
                                      ,password='0978')   
            
            inserirDados = """INSERT INTO paciente (id,nome,dt_nascimento,cpf,
            nome_mae,dt_atualizacao) VALUES (%s,%s,%s,%s,%s,%s);"""
        
            cursor = conexao.cursor()
            cursor.execute(inserirDados,(linha.split(',')))
            conexao.commit()
        except Error as erro:
            print(erro)
        
print(cursor.rowcount, "registros inseridos")
if(conexao.is_connected()):
    conexao.close()
    cursor.close()
    print("Conexão encerrada")

    
    
    # if conexao.is_connected():
    #     info = conexao.get_server_info()
    #     print("Conectado com sucesso")
    #     cursor = conexao.cursor()
    #     cursor.execute('SELECT database();')
    #     linha = cursor.fetchone()
    #     print(linha)
        
    # if conexao.is_connected():
    #     cursor.close()
    #     conexao.close()
    #     print("Conexão encerrada")