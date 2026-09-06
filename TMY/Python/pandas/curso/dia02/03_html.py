#%%

import pandas as pd

url = "https://gist.github.com/edirpedro/69c0974613de044ebba6dc7fd0c5b732"
dfs = pd.read_html(url)
dfs

# %%
dfs_uf = dfs[0]
dfs_uf.to_csv("ufs.csv",sep=";",index=False)
dfs_uf

# %%
