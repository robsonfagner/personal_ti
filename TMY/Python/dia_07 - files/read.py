#%%

nome_arquivo = "historia.txt"
#Abre o arquivo.
open_file = open(nome_arquivo)

# %%
print(open_file)
# %%

# Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)
# %%

# Fecha o Arquivo
open_file.close()
#%%
