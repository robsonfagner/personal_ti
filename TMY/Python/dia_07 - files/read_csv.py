# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines
    
print(data)
# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines()  # Correção aqui

print(data)

for linha in data:
    print(linha)

# %%

chaves = data{0}.strip("\n").split(";")

# %%
