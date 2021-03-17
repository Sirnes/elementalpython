import re
import requests

buscar = requests.get('www.google.com')
encontrar = re.findall(r'image', buscar)
teste = input('Qual seu nome?\n')

pattern = re.findall(r'[Cavaleiro]', teste)

# pattern = re.search(r'Cavaleiro', teste)  # RAW string o "r" antes de uma string a imprimir de forma crua.
# \w expecifica que é um caracter alfa-numerico tambem expecifica a quantidade de caracteres procurados dedo = \w\w\w\w  //   \w+ (tem que ter uma ou mais)  ou \w* (inclui tudo o que estiver a frente da positivo se tiver zero caracter a mais..
# No search no final de uma palavra pode se por o "." que significa qualquer caracter alfa- numerico . Mas se quiser especificar o caracter"." usa- se "\."
# \w{5} ou \w{6,8}  expecifica a quantidade  //    \w+ uma ou mais letras
# Exemplo de busca por padrão de email \w+@\w+\.\w , [\w-]+@[\w-]+\.[\w\.-]


#print("Te peguei", (pattern.group()))
# Usar apenas quando estiver utilizando o padrão re.search

print("Te peguei", (pattern))

if pattern == 'Cavaleiro':     # Ao que parece apenas vai constar se a pesquisa teve sucesso para retornar true
    print('Funcionou')
else:
    print('Deu merda')


print("\n Oi\n tudo bem\n com você\n  ?")


