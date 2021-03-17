frutas = ('laranja', 'pera', 'uva', 'banana')

# diferente da lista o valor da tupla (tuple) é imutavel.
# Util quando se deseja restringir o número de elementos.

print(frutas)

print(frutas[2])

print(frutas[:3])

if 'laranja' in frutas:
    print("Tem laranja na sacola")