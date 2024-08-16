import pandas as pd

oldData = pd.read_excel('dados_extraidos.xlsx')
for old in oldData.values:
    print(old[0])