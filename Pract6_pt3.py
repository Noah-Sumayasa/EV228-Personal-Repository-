import fnc_process_data as fncp

df = fncp.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\era5_10mwind_1980-1989.nc', 'si10', 'valid_time')

plot_df = fncp.Plot_Grid_Data(df["mean"], )

