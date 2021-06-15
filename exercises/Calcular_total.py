import pandas as pd

df = pd.read_csv('./resources/amount.csv')
total = df['mount'].sum()
print(total)