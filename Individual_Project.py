import matplotlib.pyplot as plt
import fnc_process_data as fncp
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np
import sys 
import xarray as xr
#import cartopy.crs as ccrs

latsnow, longsnow, Snowvar, snowvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_1.nc','latitude', 'longitude', 'lsf', 'valid_time')
lattemp, longtemp, Tempvar, tempvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_2.nc','latitude', 'longitude', 't2m', 'valid_time')

Snowvarstat = Snowvar.max('valid_time')

maxlatsnow = max(latsnow)
minlatsnow = min(latsnow)
maxlongsnow = max(longsnow)
minlongsnow = min(longsnow)

#print(minlatsnow)
#print(maxlatsnow)
#print(minlongsnow)
#print(maxlongsnow)

#sys.exit('Stop')

'''Baseline approach'''
#print(latsnow)
#print(longsnow)
#fncp.Plot_Grid_Data(Snowvarmean, 'title', 'C:\\Users\\Ev228\\Downloads\\EV228_Data')
#m = Basemap()
m = Basemap(projection='mill',llcrnrlat=25.0,urcrnrlat=50.0,\
            llcrnrlon=66.0,urcrnrlon=125.0,resolution='l')
m.drawcoastlines()
m.drawmapboundary(fill_color="#FFFFFF")
m.drawcountries(linewidth=0.5, linestyle='solid', color='black')
longsnowgrid, latsnowgrid = np.meshgrid(longsnow, latsnow)
x, y = m(longsnowgrid, latsnowgrid)
m.pcolor(x, y, np.squeeze(Snowvarstat), zorder = 1)
plt.colorbar(label = 'snowfall')
plt.title("Mean extreme Snowfall events in Asia")
plt.savefig('C:\\Users\\Ev228\\Downloads\\EV228_Data\\IndvPro_Snowmax', dpi=400)
plt.show()

'***************************************************************************************************'
'''extra code and past attempts'''
#m.drawrivers(color="#555555")
#m.fillcontinents(color="#888888",lake_color="#525252")
#parallels = np.arange(-90., 91., 5.)
#m.drawparallels(parallels, labels=[True, False, False, False], fontsize=10, linewidth=0.001)
#meridians = np.arange(-180., 181., 5.) # Draw meridians every 60 degrees
#m.drawmeridians(meridians, labels=[False, False, False, True], fontsize=10, linewidth=0.001)

#longsnow = np.where(longsnow > 180, longsnow-360, longsnow)
#longsnow = (longsnow + 180) % 360 - 180
#longsnow = xr.where(longsnow > 180, longsnow - 360,longsnow)
#lonsin = np.linspace(0, 360, longsnow.shape[0])
#longsnow = shiftgrid(180., longsnow, lonsin, start= False)
#x, y = m(longsnow, latsnow)
#Plot = m.contourf(x, y, Snowvarmean, levels=20, cmap= 'RdBu_r')

#sys.exit('Stop')
