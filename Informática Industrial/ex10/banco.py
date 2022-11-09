from conta import Conta
class Banco():
    def __init__(self):
        self.__senhaGerente = 5000
        self._contas = []
        # Iniciando algumas contas
        c1 = Conta(1,senha=1234,titular="João",saldoi=500)
        c2 = Conta(2,senha=4321,titular="Maria",saldoi=200)
        self._contas.append(c1)
        self._contas.append(c2)
        
    
    def mudarSenha(self):
        novaSenha = int(input('Digite a nova senha: '))
        self.__senhaGerente = novaSenha
        print('Senha alterada!')
    
    def cadastrarClientes(self):
        print('\nBem-vindo ao cadastro de novo cliente!')
        numero = int(input('Digite o número da conta: '))
        titular = input('Digite o nome do titular da conta: ')
        senha = int(input('Digite a senha da conta: '))
        conta = Conta(numero,titular,senha)
        self._contas.append(conta)
        print('Conta criada com sucesso!')
    
    def atendimento(self):
        while True:
            print('-'*40)
            print('Bem-vindo ao atendimento do banco!')
            print('-'*40)
            print('O que você deseja?')
            print('1 - Atendimento para funcionário')
            print('2 - Atendimento para cliente')
            print('3 - Sair')
            print('-'*40)
            escolha = int(input())
            
            if escolha == 1:
                senhaDigitada = int(input('Digite a senha: '))
                if senhaDigitada == self.__senhaGerente:
                    print('-'*40)
                    print('Olá, qual procedimento deseja realizar?')
                    print('1 - Mudança de senha do gerente')
                    print('2 - Cadastro de novos clientes')
                    print('-'*40)
                    escolhaFunc = int(input())
                    if escolhaFunc == 1:
                        self.mudarSenha()
                    elif escolhaFunc == 2:
                        self.cadastrarClientes()
                else:
                    print('Senha incorreta!')
            elif escolha == 2:
                acesso = False
                numeroDigitado = int(input('Digite o número da conta: '))
                for conta in self._contas:
                    if conta.numero == numeroDigitado:
                        contaCliente = conta
                        print('Olá '+contaCliente.titular+',o que deseja?')
                        acesso = True
                if acesso:
                    print('-'*40)
                    print('1 - Ver saldo')
                    print('2 - Realizar saque')
                    print('3 - Realizar deposito')
                    escolhaCliente = int(input())
                    print('-'*40)
                    if escolhaCliente == 1:
                        senhaDigitada = int(input('Digite a senha: '))
                        contaCliente.getSaldo(senhaDigitada)
                    elif escolhaCliente == 2:
                        valor = float(input('Digite o valor a ser sacado: '))
                        senhaDigitada = int(input('Digite a senha: '))
                        contaCliente.saque(senhaDigitada,valor)
                    elif escolhaCliente == 3:
                        valor = float(input('Digite o valor a ser depositado: '))
                        contaCliente.deposito(valor)
            
            elif escolha == 3:
                break


        
