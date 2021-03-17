cores = ['verde', 'azul', 'roxo', 'amarelo', 'vermelho']
passaros = ['pardal', 'culeiro', 'gaviao', 'pavao', 'urubu']

for i in enumerate(cores):
    print(i, "-->", [i])

for i in range(len(cores)):
    print(i, '-->', cores[i])

for i in [1, 2, 3, 4, 5]:
    print(i ** 2)

print(sum([i ** 2 for i in range(10)]))

print('Showing results -->', [i ** 2 for i in range(10)])

for i in range(6):
    print(i ** 2)

for i in bytearray(6):
    print(i ** 2)

for i in range(len(cores) - 1, -1, -1):
    print(cores, i)

for i in reversed(cores):
    print(i)

for a, b in zip(cores, passaros):
    print(cores, '-->', passaros)


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    elif len(c1) < len(c2):
        return 1
    return 0



