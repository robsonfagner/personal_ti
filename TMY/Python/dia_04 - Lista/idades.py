#%%

idades = [17,28,33,45,60]
print(idades)
#%%
idades.append(32)
print(idades)
# Listas são objetos mutaveis, string n é 

#%%


idades = []

while True:
    idade = input("Entre com a sua idade:")
    if idade =="": 
        break
    idades.append(int(idade))
    
print(idades)

media = sum(idades)/len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA", media)
print("MINIMO", minimo)
print("MAXIMO", max)
print("QTDE", qtde)


