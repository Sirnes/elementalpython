from tkinter import S

print("Bem vindo a um jogo super divertido para saber se um número é maior que o outro")
pergunta = input("Vamos começar? S/N ")


if pergunta == "s":
    a = int(input("Escrreva um numero: "))
    b = int(input("Escrreva um numero: "))

else:
    print("Ok, tchau, tchau seu bobão.")

while a > b:
    print("Sim, parabéns", (a), "e maior que ", (b))
    pergunta = input("Vamos brincar de novo? S/N ")
    Repeat()


def Repeat():
    while a > b:
        print("Sim, parabéns", (a), "e maior que ", (b))
        pergunta = input("Vamos brincar de novo? S/N ")
        if pergunta == "s":
            a = int(input("Escrreva um numero: "))
            b = int(input("Escrreva um numero: "))

while a < b:
    print((a), "não é maior que ", (b))
    print("Vamos tentar novamente. Vê se agora presta mais atenção!")
    a = int(input("Escrreva um numero: "))
    b = int(input("Escrreva um numero: "))