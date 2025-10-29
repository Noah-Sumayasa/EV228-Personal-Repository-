import pandas as pd
def process_data(file, variable1, variable2):
    df_cos = pd.read_csv(file)
    
    var1 = df_cos[variable1]
    var2 = df_cos[variable2]
    

