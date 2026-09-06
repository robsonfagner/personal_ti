
#%%

import pandas as pd

idades =[
           32, 38, 30, 30, 31,
           35, 25, 29, 31, 37,
           27, 23, 36, 33, 39,
]

nomes =[
    "Robson","Taissa","Jane","Davi","Arthur",
    "Gustavo","Ailton","Yasmin","Teste","Teste2",
    "Teste3","Teste4","Teste5","Teste6","Teste7",
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades
series_nomes


#%%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

#%%
df["idades"]
# %%
df.iloc[0]["nomes"]


# %%
df.iloc[-1]["idades"]