
# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:

    """ 
    Juros compostos servem para me encher o saco
     
    Aporte:Numero inteiro que represente um valor em Reais.

    Anos:Tempo em anos da função

    Taxa:Taxa mensal ou ano em porcentagem.
      
    """
    # Nome = DocString
    return aporte * (1+taxa) ** anos

# %%
juros_compostos(taxa=0.13,aporte=10000, anos=4)

# %%
