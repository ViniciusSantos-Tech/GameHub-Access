print("----Bem vindo a Lan House!----")
print("|Para Jogar, voce precisa ter 18 anos!")
def Sis():
    while True:
        global idade
        idade = int(input("|Qual sua idade?:  "))
        if idade >= 18:
            print("Voce é maior de idade")
            Horas()
            break
        else:
            print("voce é menor de idade")
def Horas(): 
    horario = int(input("Que horas são? (0-23) "))
    if horario < 23:
        print("ainda nao deu a hora do estabelecimento fechar")
    else:
        print("Ja passou da hora")

    creditos = float(input("Quantos créditos você tem? R$ "))

    if idade >= 16 and horario < 22 and creditos >= 8.0:
        print("Voce esta liberado para jogar")
Sis()
