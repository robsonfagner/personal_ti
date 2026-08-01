# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50


# texto = """ 
# Escolha sua água para comprar
# (1) Natural
# (2) Com Gás
# """

# opcao = input(texto)

# if opcao == "1":
#     print("Sua conta deu: R$1,50")

# elif opcao == "2":
#     print("Sua conta deu: R$2,50")

# else:
#     print("Entre com o caralho da opção correta !!!")

texto = """ 
Escolha sua água para comprar
(1) Natural
(2) Com Gás
"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5
elif opcao == "2":
     conta = 1.5

if conta == 0:
    print("Entre com o caralho da opção correta !!!")
else:
    print("Sua conta é de: R$", conta)