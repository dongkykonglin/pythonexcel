import os
import pandas as pd
cwd = os.path.abspath('')
files = os.listdir(cwd)
df_total = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df_total = df_total.append(pd.read_excel(file), ignore_index=True)

df_total.to_excel('AnnualBudget.xlsx')
