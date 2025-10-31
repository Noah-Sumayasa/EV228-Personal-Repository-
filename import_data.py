import pandas as pd

path_data = 'C:\\Users\\Ev228\\Downloads\\EV228_Data\\'
fn_data = 'KRDU_temp_188708-202508.csv'

df_cos = pd.read_csv(path_data + fn_data)
print(df_cos)

yr = df_cos['YEAR']
amt = df_cos['metANN']

fig = plt.figure(Output)

plt.plot(max_temp, color='red', label='max temp')
plt.xlabel('time')
plt.ylabel('temperature, deg F')
plt.legend()
plt.show()