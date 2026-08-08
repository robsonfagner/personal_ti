
# %%

def juros_compostos(aporte, taxa, anos):
    ''' 
    
    Juros compostos servem para me encher o saco
     
    Aporte:Numero inteiro que represente um valor em Reais.

    Anos:Tempo em anos da função

    Taxa:Taxa mensal ou ano em porcentagem.
      
    '''
    return aporte * (1+taxa) ** anos

# %%
juros_compostos(taxa=0.13,aporte=1000, anos=4)

#%%

# Parei no 28:54

