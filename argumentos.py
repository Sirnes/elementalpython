import sys

arguments = sys.argv  # nesse metodo o primeiro arggumento é mostrar o caminho do arquivo


def soma(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2

if arguments[1] == "soma":
    resp = soma(float(arguments[2]), float(arguments[3]))

    print(resp)

elif arguments[1] == "sub":
    resp = sub(float(arguments[2]), float(arguments[3]))

    print(resp)
