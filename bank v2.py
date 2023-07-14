print('Olá, tudo bem? Bem vindo ao Bank Marcelo da DIO!')


def deposito(saldo, extrato, /):
    print('[---------[DEPÓSITO]---------]')
    print()
    depositoValor = float(input('Digite o valor do depósito: '))
    print()

    while depositoValor <= 0:
        depositoValor = float(input('Valor inválido, Digite novamente o valor do depósito: '))

    if depositoValor > 0:
        saldo += depositoValor
        extrato += f'Depósito de: R$ +{depositoValor:.2f}\n'

        print(f'Seu saldo atual é de: R$ {saldo:.2f}')
        print()

    else:
        print('Ocorreu um erro, tente novamente!')

    return saldo, extrato


def saque(*, saldo, extrato, limite, saques, LIMITE_DO_SAQUE):
    print('[---------[SAQUE]---------]')
    print()
    sacarValor = float(input('Digite o valor que deseja sacar: '))
    while sacarValor <= 0:
        sacarValor = float(input('Valor inválido, Digite novamente o valor que deseja sacar: '))

    limiteSaldo = sacarValor > saldo
    limiteBanco = sacarValor > limite
    limiteSaques = saques >= LIMITE_DO_SAQUE

    if limiteSaldo:
        print()
        print('Ocorreu uma falha! O seu saldo é insuficiente!')
        print()

    elif limiteBanco:
        print()
        print('Ocorreu uma falha! O valor de saque é maior do que o limite do seu banco.')
        print()

    elif limiteSaques:
        print()
        print('Ocorreu uma falha! Já houveram 3 saques no dia de hoje, tente novamente amanhã.')
        print()

    elif sacarValor > 0:
        saldo -= sacarValor
        extrato += f'Saque de: R$ -{sacarValor:.2f}\n'
        saques += 1

        print(f'Seu saldo atual é de: R$ {saldo:.2f}')
        print()

    else:
        print('Ocorreu um erro, tente novamente!')

    return saldo, extrato


def ver_extrato(*, extrato):
    print('[---------[EXTRATO]---------]')
    print()
    print("Não foi realizada nenhuma movimentação." if not extrato else extrato)
    print()
    return extrato


def criar_usuario():
    pass


def criar_conta():


def menu():
    # Listas
    opcoesMenu = ['1 - Criar Usuário', '2 - Criar Conta', '3 - Listar Contas', '4 - Depositar', '5 - Sacar', '6 - Extrato', '0 - Sair']
    user_client = []
    account_client = []

    # Utilitários do Sistema
    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    LIMITE_DO_SAQUE = 3

    while True:

        print('[-------------------[MENU INICIAL]-------------------]')
        print()
        print(f'       {user} ------ [Saldo Atual: R$ {saldo:.2f}]       ')
        print(f'           Limite do Banco: R$ {limite:.2f}')
        print()
        print('Serviços disponíveis:')
        print()
        for i in range(4):
            print(opcoesMenu[i])
        print()

        try:
            opcao = int(input('Digite a opção desejada: '))
            while opcao <= 0 or opcao > 4:
                opcao = int(input('Opção inválida! Digite novamente a opção desejada: '))
            print()

            if opcao == 1:
                pass

            elif opcao == 2:
                pass

            elif opcao == 3:
                pass

            elif opcao == 4: # Função de Depósito
                saldo, extrato = deposito(saldo, extrato)

            elif opcao == 5: # Função de Sacar
                saldo, extrato = saque(saldo=saldo, extrato=extrato, limite=limite, saques=saques, LIMITE_DO_SAQUE=LIMITE_DO_SAQUE)

            elif opcao == 6: # Função do Extrato
                ver_extrato(extrato=extrato)

            else:
                print('Programa finalizado com sucesso!')
                break

        except ValueError:
            print('Esta opção é inválida, escolha uma das opções a seguir somente com números (1,2,3...)!')
            print()
menu()