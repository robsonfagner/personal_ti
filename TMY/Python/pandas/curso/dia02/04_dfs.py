#%%

import pandas as pd
df_clientes = pd.read_csv(r"C:\Users\rbsfa\Documents\Git\personal_ti\TMY\Python\pandas\curso\data\clientes.csv",sep=";")
df_clientes
# %%
df_clientes.head(n=10) #Visualiza os 10 primeiros

#%%

df_clientes.tail() #Visualiza os 10 ultimos

# %%
df_clientes.sample(10) #Visualiza aleatórios

#%%
df_clientes.shape 

#%%
df_clientes.columns

#%%
df_clientes.index
#%%
df_clientes.info()

