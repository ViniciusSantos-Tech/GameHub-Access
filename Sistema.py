idade = int(input("Qual sua idade? "))
if idade >= 18:
    print("Voce é maior de idade")
else:
    print("voce é menor de idade")

horario = int(input("Que horas são? (0-23) "))
if horario < 22:
    print("ainda nao deu a hora do estabelecimento fechar")
else:
    print("Ja passou da hora")

creditos = float(input("Quantos créditos você tem? R$ "))

if idade >= 16 and horario < 22 and creditos >= 8.0:
    print("Voce esta liberado para jogar")
