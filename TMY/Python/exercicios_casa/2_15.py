# %%
# Escreva um programa que receba uma lista de numeros do usuario e conte
# Quantas vezes um numero especifico aparece na lista e solicite o usuário um numero e exiba a contagem


lista = [1,2,1,2,1,1,1,1,1,34,1,4,5,6,3,7,8,9,90,0,3,5,5,5,]

numero = int(input("Entre com um numero: "))

contador = 0
for i in lista:
    print(i)
    
    if i == numero:
        contador += 1

print("Quantidade de: ", numero, ":" , contador)
    