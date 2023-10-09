import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

df = pd.DataFrame(data)
print(df)
print(df.iloc[0:,0])
df.index = df.iloc[0:, 0]
print(df)  # This will show the default integer-based index.
