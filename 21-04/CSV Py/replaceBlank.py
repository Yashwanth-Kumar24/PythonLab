import pandas as pd

df = pd.read_csv("sam.csv") 

#before filling NaN values
print("Before filling NaN values")
print(df)

mean_value=df['SN'].mean()
df['SN'].fillna(value=mean_value, inplace=True)

#After filling NaN values
print()
print('Updated Data!!')
print(df)
