import xarray as xr
import matplotlib.pyplot as plt

data_set= xr.open_dataset('C:\\Users\\Ev228\\Downloads\\EV228_Data\\' + '9b653170ac34b5b85cd994a4395e052b.nc')
'''
Imports the netCDF file and parses the data for the t2m data and graphs it

Arguments: 

'''
var1= data_set['t2m']

var1_ave= var1.mean('valid_time')

var1_ave.plot()
#print(data_set)

plt.show()