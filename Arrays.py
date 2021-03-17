testando = ['Junior', 'Carlos', 'Pedro', 'Eduardo', 'Pedro', 'Jeronio', 'Pedro', 'Miguel']

loucura = 'TODO MUNDO LOUCO O MUNDO VIROU UMA LOUCURA'

mais_loucura = 'TODO, MUNDO, LOUCO, O, MUNDO, VIROU, UMA, LOUCURA'

robots = 'Eu adoro robots porque eles sao muito legais'

passando_a_Letra = testando.count('Pedro')  # este método conta quantas vezes um objeto é mencionado em uma lista

print(type(testando[0:2]))  # Imprime o tipo de dados

print(testando[0:2])

print(len(robots))  # len imprime o tamanho

print((robots[0:30:2]))  # O terceiro numero dita o intervalo.

print(testando[-1])  # Começa a contar atravez do ultimo valor.

print(robots[::])  # imprime todos os itens.

print(robots[::-1])  # Imprime todos os itens com a ordem inversa.

testando.append('Zarabatel')  # acrescenta um item a lista

print(testando)

testando.remove("Miguel")  # remove um item a lista.

print(testando)

testando.insert(0, "BUTAREL_ZAFA")  # Expecifica o local para inserir o item.

print(testando)

print(passando_a_Letra)

print(len(testando))

print(testando.pop())  # Pega o ultimo nome da Lista e remove.

print(testando)

print(loucura.lower())

print(loucura.upper())

changes = mais_loucura.split(',')  # transforma uma string em uma lista podendo expecificar o elemento que marca a separação;

print(changes)

print(len(changes))


