
# %%

def juros_compostos(aporte, taxa, anos):
    return aporte * (1+taxa) ** anos

# %%
juros_compostos(taxa=0.13,aporte=1000, anos=4)


