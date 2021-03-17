import random

bluehead = ['Dionis', 'Gerhard', 'Donald', 'William', 'David']
spam = 'Tocando o foda se mais uma vez'
i = 0
count = 0

while i < 10:
    print(i, spam)
    i = i + 1

for i in range(1, 10, 2):
    count = count + i
    print(count)

print(len(bluehead))

for i in range(len(
        bluehead)):  # Marca o número de vezes que sera dado o print de acordo com o a função len sobre a variavel bluehead
    print(bluehead[i])  # Com a definição do [i] para cada print dado sera uma chave da lista.

print(len(spam))


for i in range(len(bluehead)):  # Marca o número de vezes que sera dado o print de acordo com o a função len sobre a variavel bluehead
    bluehead.append('foda- se')     # Sera adicionado o 'foda- se' cinco vezes.
    print(bluehead)  # Nesse caso sera impresso a lista bluehead completa por 5 vezes.

for i in range(10):
    x = random.random()
    print(x)

