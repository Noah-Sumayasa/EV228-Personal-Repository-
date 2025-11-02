import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import fun_eds

lat = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-eDNA-Download.csv', 'Latitude')
long = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-eDNA-Download.csv', 'Longitude')

print(lat)
print(long)

#plt.plot(long, lat)
#plt.show()

#plt.scatter(long, np.arange(0, np.size(long)), s=35, color='red', marker='.', label='longitude')
#plt.show()

