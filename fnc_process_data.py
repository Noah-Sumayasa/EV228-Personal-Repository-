import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

def process_data(file, variable1, variable2, Title_String, Label_Stringx, Label_Stringy):
    df_cos = pd.read_csv(file)
    ''' Imports data file and returns the data parsed from the column specified

    Arguments:
    file -- the path name that directs to the data set desired 
    variable1 -- when set to a specific string, parses for that in the file
    variable2 -- when set to a specific string, parses for that in the file

    Outputs:
    var1 -- the data parsed indicated at the string in variable1
    var2 -- the data parsed indicatated at the string in variable2
    '''
    var1 = df_cos[variable1]
    var2 = df_cos[variable2]
    var3 = pd.concat([var1, var2], axis= 1)
    var3_filtered = var3[var3[variable2]!= 999.90]
    
    print(var3_filtered)
   # fig = plt.figure()

    var3_filtered.set_index(variable1, inplace = True)
    var3_filtered.plot()
    plt.xlabel(Label_Stringx)
    plt.ylabel(Label_Stringy)
    plt.legend()
    plt.show()
    


def process_grid_data(path_file, variable1, validtime):
    data_file= xr.open_dataset(path_file)
    var1= data_file[variable1]
    var2= data_file[validtime]

    '''
Imports the netCDF file and parses the data for the t2m data and graphs it

Arguments: 

'''
    
    var2_ave= var2.mean(validtime)

    var2_ave.plot()
    plt.show()
    return var2_ave

#print(data_set)

    