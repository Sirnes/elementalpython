print("\n\n$$$$ Venda de Empadinhas Fresquinhas Feitas na Hora $$$$")
print('\nDeixaremos o Sr(a) escolher a empadinha de sua preferência')
print('\n      R$ 4,90 cada')


def value():
    valor = float(input('Por favor, digite um valor:\n R$  '))
    sub = 4.90 - valor
    soma = valor - 4.90
    if valor > 4.90:
        print('O seu troco é R$', soma, '\n **** Obrigado pela sua preferência. Volte sempre! ****')
    while valor < 4.90:
        print('Valor insuficiente. Ainda faltam R$:', sub, float('Por favor, digite um valor:\n R$  '))


def error():
    erro = input\
        ('Parece que você não entendeu direito. Você esta diante das empadinhas do seu sonho \nVamos recomeçar(s/n):\n')
    if erro == 'n':
        print('Não sabe o que esta perdendo. Tenha um bom dia e volte sempre.')
    while erro == 's':
        vendas()


def vendas():
    numero = input\
        ('\n 1 - Empadinha de frango\n\
 2 - Empadinha de carne\n 3 - Empadinha de queijo\n\n Digite o número de sua empadinha:\n>>')

    if numero == '1':
        print('\nParabéns você acabou de adguirir uma empadadinha de frango feita na hora.')
        pag = input('\nUltima etapa\n\n Qual a forma de pagamento de sua preferência?\n\n 1 - Dinheiro\n 2 - Cartão\n>>')
        if pag == '1':
                value()
    elif numero == '2':
        print('Parabéns você acabou de adguirir uma empadadinha de carne feita na hora.')
        pag = input(
            '\nUltima etapa\n\n Qual a forma de pagamento de sua preferência?\n\n 1 - Dinheiro\n 2 - Cartão\n>>')
        if pag == '1':
            print('\n **** Obrigado pela sua preferência. Volte sempre! ****')
    elif numero == '3':
        print('Parabéns você acabou de adguirir uma empadadinha de queijo feita na hora.')
        pag = input(
            '\nUltima etapa\n\n Qual a forma de pagamento de sua preferência?\n\n 1 - Dinheiro\n 2 - Cartão\n>>')
        if pag == '1':
            print('\n **** Obrigado pela sua preferência. Volte sempre! ****')
    else:
        error()


vendas()
