texto = """ 
Escolha sua água para comprar
(1) Natural
(2) Com Gás
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
     valor_item = 1.5
else:
     print("Favor digitar o valor correto!! ")

qtde = input("Quantas garrafas ?")
qtde = int(qtde)
valor_total = valor_item*qtde  

print("Sua conta deu: R$:", valor_total)
