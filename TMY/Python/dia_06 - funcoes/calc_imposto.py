#%%

def calc_imposto(preco:float, tx_base:float, **kwargs)-> float:
    imposto = preco * tx_base

#%%
calc_imposto(100, 0.3)

# %%
