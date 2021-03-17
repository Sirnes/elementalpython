var1 = 'how are you?'


def sayHello():
    print('hello')


print(var1)

sayHello()


def soma(var1, var2):
    resp = var1 + var2

    return resp


def setiver(words):

    if len(words) == 6:
        return True
    else:
        return False


print(soma(1, 2))

dados = soma(34, 3)

print(dados)

test = setiver('tudoii')

print(setiver('sdf'))

print(test)
