import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def process_data(file, variable1, variable2):
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
    return var1, var2

def plot_data(Output):
    fig = plt.figure()

    plt.plot(Output, color='red', label=str(Variable1))
    plt.xlabel(str(variable1))
    plt.ylabel('temperature, deg F')
    plt.legend()
    plt.show()
    
