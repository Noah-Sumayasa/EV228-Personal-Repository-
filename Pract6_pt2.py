import fnc_process_data as fncp
import numpy as np

df = fncp.process_data_graph('C:\\Users\\Ev228\\Downloads\\EV228_Data\\SGM00061600_temp_189201-202508.csv', 'YEAR', 'metANN', 'Sir Seewoosagur Ramgoolam International Airport 1892-2025', 'Year', 'Ave Annual Temp (deg C)')
print(df)
df_mean = df.mean()
df_STD = df.std()
df_max = df.max()
df_min = df.min()

print(df_mean)
print(df_STD)
print(df_max)
print(df_min)