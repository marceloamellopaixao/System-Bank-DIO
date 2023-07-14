opcoesMenu = ['1 - Depositar', '2 - Sacar', '3 - Extrato', '4 - Sair']
saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_DO_SAQUE = 3

print('Olá, tudo bem? Bem vindo ao Bank Marcelo da DIO!')
print('Para que necessitamos continuar, informe o dado a seguir...')
print()
user = input('Digite seu nome de usuário do banco: ')
print()


def menu():

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


menu()

while True:
    try:
        opcao = int(input('Digite a opção desejada: '))
        while opcao <= 0 or opcao > 4:
            opcao = int(input('Opção inválida! Digite novamente a opção desejada: '))
        print()

        if opcao == 1:
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
                menu()

            else:
                print('Ocorreu um erro, tente novamente!')

        elif opcao == 2:
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
                menu()

            elif limiteBanco:
                print()
                print('Ocorreu uma falha! O valor de saque é maior do que o limite do seu banco.')
                print()
                menu()

            elif limiteSaques:
                print()
                print('Ocorreu uma falha! Já houveram 3 saques no dia de hoje, tente novamente amanhã.')
                print()
                menu()

            elif sacarValor > 0:
                saldo -= sacarValor
                extrato += f'Saque de: R$ -{sacarValor:.2f}\n'
                saques += 1

                print(f'Seu saldo atual é de: R$ {saldo:.2f}')
                print()
                menu()

            else:
                print('Ocorreu um erro, tente novamente!')

        elif opcao == 3:
            print('[---------[EXTRATO]---------]')
            print()
            print(extrato)
            print()
            menu()

        else:
            print('Programa finalizado com sucesso!')
            break

    except ValueError:
        print('Esta opção é inválida, escolha uma das opções a seguir somente com números (1,2,3...)!')
        print()
        menu()
