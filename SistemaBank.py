Menu = """

[D] Deposito
[S] Saque
[E] Extrato
[X] Sair

"""


Limites_Saques = 3
Saques = 0
Limite = 500
Saldo = 0
Extrato = ''

while True:

    Opção = input(Menu)

    if Opção == 'D':
        valor = float(input("Qual quantia deseja depositar? "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Deposito: R$ {valor:.2f}\n"

    elif Opção == 'S':
        valor = float(input("Qual quantia deseja sacar? "))

        Sem_Saldo = valor > Saldo

        Limite_Saque = Saques >= Limites_Saques

        Passou_Limite = valor > Limite

        if Sem_Saldo:
            print("Saldo insuficiente")

        elif Limite_Saque:
            print("Limite de saque diáio atingido")

        elif Passou_Limite:
            print("O valor excede o limite permitido para sacar")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            Saques += 1

        else:
            print("Valor não aceito")

    elif Opção == 'E':

        print('\n===============Extrato===============')
        print('Seu extrato está vazio' if not Extrato else Extrato)
        print(f'Saldo: R$ {Saldo:.2f}\n')
        print('=====================================')

    elif Opção == 'X':
        print('Obrigado por usar nossos serviços')
        break

    else:
        print("Insira um opção válida")
