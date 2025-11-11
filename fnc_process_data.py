import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import scipy.stats as scp
from mpl_toolkits.basemap import Basemap, shiftgrid

def process_data(file, str_grab):
    data_grab = pd.read_csv(file)
    val1 = data_grab[str_grab]
    val1_filt = val1[val1 != 999.90]
    return val1_filt
    
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
    #print(var3_filtered)
    #regressline = scp.linregress(var3_filtered['YEAR'],var3_filtered['metANN'])
    plt.title(Title_String)
    plt.xlabel(Label_Stringx)
    plt.ylabel(Label_Stringy)
    plt.legend()
    plt.show()
    plt.savefig('C:\\Users\\Ev228\\Downloads\\EV228_Data')
    return var3_filtered, 


def process_grid_data_dict(path_file, variable1, variable2):
    data_file= xr.open_dataset(path_file)
    var1= data_file[variable1]
  
    #print(var1)
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

def Plot_Grid_Data(dict_val, title, filepath):
    
    dict_val.plot()
    plt.title(title) 
    #plt.xlabel(x_ax)
    #plt.ylabel(y_ax)
    plt.savefig(filepath, dpi=400)
    plt.show()
    

'''
Imports a certain value from the dictionary and plots it on a gridded format 

Arguments: 
    dict_val -- a certain key from the dictionary 

Outputs: 
    plot.show() -- plots that key from the dictionary
'''

def process_grid_data(filepath, latitude, longitude, test_variable, Year):

    data_file= xr.open_dataset(filepath)
    lat = data_file[latitude]
    long = data_file[longitude]
    var_test = data_file[test_variable]
    time = data_file[Year]

    return lat, long, var_test, time

def basemap_grid_plot(long, lat, data, timestring, cblabel, title, fp_and_name):
    Varstat = data.max(timestring)

    maxlat = max(lat)
    minlat = min(lat)
    maxlong = max(long)
    minlong = min(long)

    '''Baseline approach'''

    m = Basemap(projection='mill',llcrnrlat=minlat,urcrnrlat=maxlat,\
            llcrnrlon=minlong,urcrnrlon=maxlong,resolution='l')
    m.drawcoastlines()
    m.drawmapboundary(fill_color="#FFFFFF")
    m.drawcountries(linewidth=0.5, linestyle='solid', color='black')
    longsnowgrid, latsnowgrid = np.meshgrid(long, lat)
    x, y = m(longsnowgrid, latsnowgrid)
    m.pcolor(x, y, np.squeeze(Varstat), zorder = 1)
    plt.colorbar(label = cblabel)
    plt.title(title)
    plt.savefig(fp_and_name, dpi=400)
    plt.show()