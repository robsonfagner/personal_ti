# %%

lista = [2,132,"Robson"]
lista[2] # indice da lista


# %%
# pares de chaves valor
dados_robson = {
    "sobrenome":"fagner",
    "nome":"Robson",
    "Formação":["Engenharia civil","Edificações","Inteligencia Artificial"],
    
    "cargos":[
        {"nome":"Atendente de restaurante","Empresa":"Arcos Dourados"},
        {"nome":"Vendedor interno","Empresa":"Gimba"},
        {"nome":"Op Tlmk","Empresa":"Shoptime"},
    ]
}

# %%
print(dados_robson)
print(dados_robson["Formação"][-1])
print(dados_robson["cargos"][-1]["Empresa"])

# %%
# Inclusão de novo dado ao dicionário
dados_robson["Estado Civil"] = "casado"
# %%
dados_robson.keys()
# %%
print("Chaves:", dados_robson.keys())
print(dados_robson.values())
print("Items:", dados_robson.items())

# %%

for i in dados_robson:
    print(i, "->", dados_robson[i])

# %%

for chave in dados_robson:
    print(chave, "->",dados_robson[chave])
# %%
for item in dados_robson.items():
     print(item)
#%%
for[chave, valor] in dados_robson.items():
    print(chave, "->", valor )

# %%


