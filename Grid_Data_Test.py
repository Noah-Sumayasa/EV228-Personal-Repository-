import fnc_process_data as fncpr

GridOutput = fncpr.process_grid_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\9b653170ac34b5b85cd994a4395e052b.nc', 't2m', 'valid_time')

Plot_Data = fncpr.Plot_Grid_Data(GridOutput['max'])