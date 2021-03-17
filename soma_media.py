n1 = int(input('Digite um número\n'))

n2 = int(input('Digite outro número\n'))

test = 2

soma = n1 + n2

media = (n1+n2)/2

# print('o resultado da soma dos valores é', soma, 'e a média é', media)

print('o resultado da soma dos valores é {} e a média é {}'.format(soma, media))

# Também pode ser expecificado o numero da variavel que estara entre exp: {0} e {1}.
#  Como nas listas, se começa a contar apartir do digito 0.

# use o is para testar tipos

print(test.isnumeric()) # Não esta funcionando na minha versão do Python atual.
