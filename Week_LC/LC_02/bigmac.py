import pandas as pd

df = pd.read_csv("Week_LC/LC_02/BigmacPrice.csv")

print(df.head())
print(df.shape())

df.info()