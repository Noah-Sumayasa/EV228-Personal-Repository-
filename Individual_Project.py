import matplotlib.pyplot as plt
import fnc_process_data as fncp

grid_data = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\dat_fil_1.nc', 'lsf', 'valid_time')
grid_data2 = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\dat_fil_2.nc', 't2m', 'valid_time')
#print(grid_data)

fncp.Plot_Grid_Data(grid_data['mean'], 'title', 'C:\\Users\\Ev228\\Downloads\\EV228_Data')
