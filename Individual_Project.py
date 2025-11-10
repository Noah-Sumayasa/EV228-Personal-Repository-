import matplotlib.pyplot as plt
import fnc_process_data as fncp
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np

latsnow, longsnow, Snowvar, snowvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_1.nc','latitude', 'longitude', 'lsf', 'valid_time')
lattemp, longtemp, Tempvar, tempvalt = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Da_2.nc','latitude', 'longitude', 't2m', 'valid_time')

Snowvarmean = Snowvar.mean('valid_time')
#print(grid_data)

#fncp.Plot_Grid_Data(grid_data['mean'], 'title', 'C:\\Users\\Ev228\\Downloads\\EV228_Data')
topoin,lons = shiftgrid(-180.,Snowvar,longsnow,start=False)

m = Basemap(projection='mill',llcrnrlat=29-1,urcrnrlat=54 +1,\
            llcrnrlon=-122 -1,urcrnrlon=-66 +1,resolution='l')
m.drawcoastlines()
#m.drawrivers(color="#555555")
m.fillcontinents(color="#888888",lake_color="#525252")
m.drawmapboundary(fill_color="#383838")
#m.scatter(lon, lat, s=35, c= year, marker='x',cmap= 'copper', latlon=True)
#parallels = np.arange(-90., 91., 5.)
#m.drawparallels(parallels, labels=[True, False, False, False], fontsize=10, linewidth=0.001)
#meridians = np.arange(-180., 181., 5.) # Draw meridians every 60 degrees
#m.drawmeridians(meridians, labels=[False, False, False, True], fontsize=10, linewidth=0.001)
m.pcolor(longsnow,latsnow,np.squeeze(Snowvarmean))
plt.colorbar(label = 'snowfall')
plt.title("Mean extreme Snowfall events in North America")
plt.show()