# %%

# Uma maneira de definir listas
idades = [28, 42, 43, 40, 35, 29, 38]
print(idades)
# Dados que por acaso são inteiros

# %%
robson = ["Fagner", "Pinheiro", "40", "Casado"]
print(robson)

# %%
type(robson)
# %%

robson[1]  # Forma de acessar o elemento, o indice inicia-se no elemento (0) ZERO

print(robson[2])
robson[2]

# %%

idades = [28, 42, 43, 40, 35, 29, 38]
sum(idades)

print("qtde dados: ", len(idades))

print("A soma das idades é:", sum(idades))

print("A media das idades é:", sum(idades) / len(idades))

# print("A media das idades é:", avg(idades)) Não tem média no Python

print("A menor das idades é:", min(idades))

print("A maior das idades é:", max(idades))

# %%

robson = [
    "Fagner",
    "Pinheiro",
    "40",
    "Casado",
    ["Analista de Suporte","Estagiario", "Militar", "Engenheiro", "Resp. Técnico"],
    [1500,3200,4000,6000,8000],
    ["Davi", "Taissa", "Janes"]]  # 6 elements

print("O Tamanho do Robson é: ", len(robson))

print(robson[5][2])

fam = robson[5]
prim_fam = fam[0]
print("O primeiro membro de sua familia é o:", prim_fam)



# %%

tamanho = len(robson)
pos = tamanho - 1 #Pega o ultimo

fam = robson[pos]
robson[pos][len(fam)-1]

# %%
robson[-1][-2]

# %%

# Começa a falar sobre Fatiamento

robson[0:3] # Elementos abertos, ou seja, 3 posições

robson[4][2:5] # Sempre ignora um ou seja, 5-2 = 3

#%%

robson[4][-2:]

robson[:4] #[start:stop]

robson[1:3]

#%%

salarios = robson[5]
salarios[::-1]
#robson [ start:stop : step]


# %%
