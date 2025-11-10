import fnc_process_data as fncp
import scipy.stats as sp
import matplotlib.pyplot as plt
Output1 = fncp.process_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\KRDU_temp_188708-202508.csv','metANN')
Output2 = fncp.process_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\KRDU_temp_188708-202508.csv','YEAR')

regression = sp.linregress(Output1,Output2)
''' 
imports the function indicated by the file name "fnc_process_data" as "fncp" and runs it with the chosen data

Arguments:

'''

plt.scatter(Output2, Output1)
plt.show()
plt.show(regression)

#print(regression)
