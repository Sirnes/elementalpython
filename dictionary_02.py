tuple = ()
list = []
dict = {}
conjuntos = set()

carros = {'monza': 'preto', 'fusca': 'branco', 'chevette': 'azul'}
passaros = ['verde', 'amarelo', 'azul', 'roxo', 'laranja']
cidades = {'Nilópolis', 'Itaperuna', 'Petrópolis', 'Magé'}

for i in enumerate(carros):
    print(i, carros.keys(), '-->', i)

if 'monza' in carros:
    print("O carrão esta pronto")

if 'verde' in passaros:
    print("Esta")

for x in carros.values():
    print(x)

for x in carros.keys():
    print(x)

for x in carros.copy():
    print(x)

if 'preto' not in passaros:
    print("Não esta")

print(carros)

carros['monza'] = 'rosa'

print(carros)

carros['Jeep'] = 'cor das matas'

print(carros)

print(cidades)

cidades.remove('Magé')

print(cidades)

cidades.add('Santo Antônio de Pádua')

print(cidades)

del carros['Jeep']

print(carros)