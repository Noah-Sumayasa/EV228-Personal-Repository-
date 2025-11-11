import matplotlib.pyplot as plt
import fnc_process_data as fncp
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np
import sys 
#import cartopy.crs as ccrs

latsnow, longsnow, Snowvar, snowvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_1.nc','latitude', 'longitude', 'lsf', 'valid_time')
lattemp, longtemp, Tempvar, tempvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_2.nc','latitude', 'longitude', 't2m', 'valid_time')

Snowvarmean = Snowvar.mean('valid_time')


'''Baseline approach - which isn't working'''
print(latsnow)
print(longsnow)

#fncp.Plot_Grid_Data(Snowvarmean, 'title', 'C:\\Users\\Ev228\\Downloads\\EV228_Data')

#sys.exit('Stop')

#Wraplon = (longsnow + 180) % 360 - 180
#longsnow2 = Wraplon.sortby(longsnow)
#Wraplat = (latsnow + 180) % 360 -180
#latsnow2 = Wraplat.sortby(latsnow)
#lonsin = np.linspace(66., 125.)
#longsnow2 = shiftgrid(180., longsnow, lonsin, start=False)

#m = Basemap(projection='lcc',llcrnrlat=29-1,urcrnrlat=54 +1,\llcrnrlon=-122 -1,urcrnrlon=-66 +1,resolution='l')
#x,y = m(longsnow.data, latsnow.data)
m = Basemap()
m.drawcoastlines()
#m.drawrivers(color="#555555")
m.fillcontinents(color="#888888",lake_color="#525252")
m.drawmapboundary(fill_color="#383838")
#parallels = np.arange(-90., 91., 5.)
#m.drawparallels(parallels, labels=[True, False, False, False], fontsize=10, linewidth=0.001)
#meridians = np.arange(-180., 181., 5.) # Draw meridians every 60 degrees
#m.drawmeridians(meridians, labels=[False, False, False, True], fontsize=10, linewidth=0.001)
m.pcolor(longsnow, latsnow,np.squeeze(Snowvarmean), zorder = 1000)
#Plot = m.contourf(longsnow, latsnow, Snowvar, levels=20, cmap= 'RdBu_r')

plt.colorbar(label = 'snowfall')
plt.title("Mean extreme Snowfall events in North America")
plt.show()