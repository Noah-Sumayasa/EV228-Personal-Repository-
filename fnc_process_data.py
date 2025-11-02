import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr


def process_data(file, str_grab,):
    data_grab = pd.read_csv(file)
    val1 = data_grab(str_grab)
    return val1
''' Imports data file and returns the data parsed from the specific column
    
    Arguments: 
        file -- the path name that directs to the data set desired
        str_grab --  when set to a specific string, parses for that in the file

    Outputs 
        val1 -- returns data parsed in the column specified
    
'''
                
def process_data_graph(file, variable1, variable2, Title_String, Label_Stringx, Label_Stringy):
    df_cos = pd.read_csv(file)
    ''' Imports data file and plots the data parsed from the column/s specified

        Arguments:
            file -- the path name that directs to the data set desired 
            variable1 -- when set to a specific string, parses for that in the file
            variable2 -- when set to a specific string, parses for that in the file
            Title_String -- Specific string for the graph title
            Label_Stringx -- Specific string for x axis
            Label Stringy -- Specific string for y axis

        Outputs:
            plot() -- plots the data parsed
    '''
    var1 = df_cos[variable1]
    var2 = df_cos[variable2]
    var3 = pd.concat([var1, var2], axis= 1)
    var3_filtered = var3[var3[variable2]!= 999.90]
    
    #print(var3_filtered)
   # fig = plt.figure()

    var3_filtered.set_index(variable1, inplace = True)
    var3_filtered.plot()
    plt.title(Title_String)
    plt.xlabel(Label_Stringx)
    plt.ylabel(Label_Stringy)
    plt.legend()
    plt.show()
    


def process_grid_data(path_file, variable1, variable2):
    data_file= xr.open_dataset(path_file)
    var1= data_file[variable1]
  
    print(var1)
    '''
Imports the netCDF file and parses the data for the t2m data and graphs it

Arguments: 
    path_file -- the path name that directs to the data set desired 
    variable1 -- when set to a specific string, parses for that in the file
    variable2 -- when set to a specific string, parses for that in the file

Outputs: 
    dict_grid -- outputs the dictionary of values calculated with descriptive statistics 
'''
    dict_grid = {
        "mean": var1.mean(variable2),
        "STD": var1.std(variable2),
        "median": var1.median(variable2),
        "max": var1.max(variable2),
        "min":var1.min(variable2)
        #"Quan": var1.quantile(validtime, 0.5)
    }
    return dict_grid

#print(data_set)

def Plot_Grid_Data(dict_val):
    
    dict_val.plot()
    plt.show()

'''
Imports a certain value from the dictionary and plots it on a gridded format 

Arguments: 
    dict_val -- a certain key from the dictionary 

Outputs: 
    plot.show() -- plots that key from the dictionary
'''
    