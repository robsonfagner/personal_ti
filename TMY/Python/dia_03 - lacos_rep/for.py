# %%
nome = "Robson Fagner"
for letra in nome: # Letra var temp, que percorre toda a var que foi chamada logo acima
                   # for percorre os elementos de um objeto.
    print(letra)        
#%%
numero = 2
max_numero = 100

for i in range(1, max_numero + 1): #range cria uma sequencia
    print(numero, "x" , numero * i)   
#%%

for i in range(4,101):
    if i % 4 == 0:
        print (i) 
