# Implementar apenas 3 operações no banco: DEPOSITO, SAQUE e EXTRATO.
# Ter um usuário (Opcional)

opcoesMenu = ['[1] - Depósito', '[2] - Saque', '[3] - Extrato', '[0] - Sair']
LIMITE = 500.00


# Opções do Menu
def opcoes_menu():
    for i in range(4):
        print(opcoesMenu[i])


def linha():
    print('[' + ('-' * 40) + ']')

# user = input('Digite seu nome: ')
print()


def menu():
    linha()
    print('[-----------------[MENU]-----------------]')
    linha()
    print()

    opcoes_menu()
    print()


menu()
