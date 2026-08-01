#Faça um programa que receba 4 alturas usando um laço de repetição e 
#realize a soma dessas alturas.

#%%
soma = 0 # Valor final

qtde_entradas = 4 # contador de entradas

for i in range(qtde_entradas):
    altura = input("Entre com a sua altura: ")
    altura = float(altura)
    soma += altura
    print("soma das alturas: ", soma)