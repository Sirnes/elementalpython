carros = {'monza': 'preto', 'fusca': 'branco', 'chevette': 'azul'}  # hash table, dict (python).
# Dicionários não são ordenados. Não possuem indice exp: print(carros[1]) -- log error

conjunto = {'monza', 'fusca', 'chevette'}  # O conjunto (set em Python) é parecido com a lista
#  com a diferença que não se
# pode ter chaves repetidas. Se houver eles serão desconsiderados. Conjuntos também não tem chaves +
# valores como nos dicionários. Conjuntos não são ordenados. Não possuem indice exp: print(conjunto[1])-- log error

print(carros)

print(carros['monza'])  # Ao definir a chave no print ele demonstra o valor.

for i in carros:
    print(i)

carros.copy()

passaros = ['verde', 'amarelo', 'azul', 'roxo', 'laranja']

print(passaros)

passaros[0] = 'violeta'     # Muda a chave segundo o índice.

print(passaros)

passaros.extend('cachorro')     # Que louco isso aqui.

print(passaros)

passaros.append('porco')     # Que louco isso aqui.

print(passaros)

for i in passaros:
    print(len(passaros))
    print('ferrou geral')
    i = i
    print(i)


if 'verde' in passaros:
    print("Esta")