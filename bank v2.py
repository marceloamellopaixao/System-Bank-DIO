print('Olá, tudo bem? Bem vindo ao Bank Marcelo da DIO!')
print()


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
        print()
        print('Ocorreu um erro, tente novamente!')
        print()

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
        print()
        print('Ocorreu um erro, tente novamente!')
        print()

    return saldo, extrato


def ver_extrato(*, extrato):
    print('[---------[EXTRATO]---------]')
    print()
    print("Não foi realizada nenhuma movimentação." if not extrato else extrato)
    print()
    return extrato


def criar_usuario(user_clients):
    print('[---------[NOVO USUARIO]---------]')
    print()
    cpf = input('Digite o CPF (somente numeros): ')
    user = filtro_account(cpf, user_clients)

    if user:
        print()
        print(f'Erro! Já existe um usuário com este CPF!')
        print()
        return

    else:
        nome = input('Digite o seu nome completo: ')
        dt_nasc = input('Digite sua data de nascimento (dia/mes/ano): ')
        endereco = input('Digite seu endereço (logradouro, numero - bairro - cidade/UF): ')

        user_clients.append({'nome': nome, 'data_nasc': dt_nasc, 'cpf': cpf, 'endereco': endereco})
        print()
        print('[=]--[Conta Criada com Sucesso]--[=]')
        print()


def criar_conta(agencia, num_accounts, user_clients):
    print('[---------[NOVA CONTA]---------]')
    print()
    cpf = input('Digite o CPF (somente numeros): ')
    user = filtro_account(cpf, user_clients)

    if user:
        print()
        print('[=]--[Conta Criada com Sucesso]--[=]')
        print()
        return {'agencia': agencia, 'num_account': num_accounts, 'user_client': user}

    else:
        print()
        print('[!]--[Este usuário não foi localizado, crie um usuário e tente novamente]--[!]')
        print()


def filtro_account(cpf, user_clients):
    user_filters = [user for user in user_clients if user['cpf'] == cpf]
    return user_filters[0] if user_filters else None


def exibir_contas(account_clients):
    print('[' + (10 * '-') + "CONTAS CADASTRADAS" + (10 * '-') + ']')
    print()

    if len(account_clients) == 0:
        print("Não foi localizada nenhuma conta, Crie já!", account_clients)
        print()

    else:
        print(account_clients)

        for account in account_clients:
            recents_account = f"Agência: {account['agencia']}\n"\
                              f"Conta: {account['num_account']}\n" \
                              f"Usuário: {account['user_client']['nome']}"
            print(recents_account)
            print()


def menu():
    # Listas
    opcoesMenu = ['1 - Criar Usuário', '2 - Criar Conta', '3 - Listar Contas', '4 - Depositar', '5 - Sacar',
                  '6 - Extrato', '0 - Sair']
    user_clients = []
    account_clients = []

    # Utilitários do Sistema
    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    LIMITE_DO_SAQUE = 3

    user_act = 'Crie seu usuário'
    AGENCIA = '0001'

    while True:

        print('[-------------------[MENU INICIAL]-------------------]')
        print()

        for user in user_clients:
            if user:
                user_act = f"{user['nome']}"
            else:
                print('Usuário não encontrado')

        print(f'       {user_act} ------ [Saldo Atual: R$ {saldo:.2f}]       ')
        print(f'           Limite do Banco: R$ {limite:.2f}')
        print()
        print('Serviços disponíveis:')
        print()
        for i in range(7):
            print(opcoesMenu[i])
        print()

        try:
            opcao = int(input('Digite a opção desejada: '))
            while opcao < 0 or opcao > 6:
                opcao = int(input('Opção inválida! Digite novamente a opção desejada: '))
            print()

            if opcao == 1:  # Função de Criar Usuário
                criar_usuario(user_clients)

            elif opcao == 2:  # Função de Criar Conta
                num_accounts = len(account_clients) + 1
                account_client = criar_conta(AGENCIA, num_accounts, user_clients)

                if account_client:
                    account_clients.append(account_client)

            elif opcao == 3:  # Função de Contas
                exibir_contas(account_clients)

            elif opcao == 4:  # Função de Depósito
                saldo, extrato = deposito(saldo, extrato)

            elif opcao == 5:  # Função de Sacar
                saldo, extrato = saque(saldo=saldo, extrato=extrato, limite=limite, saques=saques,
                                       LIMITE_DO_SAQUE=LIMITE_DO_SAQUE)

            elif opcao == 6:  # Função do Extrato
                ver_extrato(extrato=extrato)

            else:
                print('Programa finalizado com sucesso!')
                break

        except ValueError:
            print('Esta opção é inválida, escolha uma das opções a seguir somente com números (1,2,3...)!')
            print()


menu()
