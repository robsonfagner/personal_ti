fruta = input("Digit aqui sua fruta: ")

frutas = {
    "Maçã": "R$1,50",
    "Banana": "R$2,75",
    "Uva": "R$1,90",
    "Pera": "R$1,25",
    "Laranja": "R$0,65",
    "Limão": "R$1,25",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,20",
    "Jaca": "R$5,80",
}
if fruta in frutas:
  print(frutas[fruta])
else:
    ("Entre com um valor válido!!!")