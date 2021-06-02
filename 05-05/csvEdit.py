import pandas as pd

csv_filename = "demo.csv"
file =pd.read_csv(csv_filename)

file.fillna(value="NULL", inplace=True)

columns = file.columns.values.tolist()
file_mean = file.groupby(columns)[['total_mean']].mean()
file_mean = file_mean.reset_index()
