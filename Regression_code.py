import fnc_process_data as fncp
import scipy.stats as sp
import matplotlib.pyplot as plt
import sys
import numpy as np
Output1 = fncp.process_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Bishop-Rock.csv','T_HMP')
Output2 = fncp.process_data('C:\\Users\\Ev228\\Downloads\\EV228_Data\\Bishop-Rock.csv','TIMESTAMP')

#max = Output2.max()
#min = Output2.min()
#print(min)
#print(max)

#mean = Output1.mean() 
#STD = Output1.std()
#max = Output1.max()
#min = Output1.min()

#print(mean)
#print(STD)
#print(max)
#print(min)

Reg = sp.linregress(Output2, Output1)
print(Reg)

sys.exit('Stop') 

slope = Reg.slope
intercept = Reg.intercept
y_pred = intercept + slope * Output2
''' 
imports the function indicated by the file name "fnc_process_data" as "fncp" and runs it with the chosen data

Arguments:

'''

plt.scatter(Output2, Output1)
plt.plot(Output2, y_pred, color='red', label='Regression Line')
plt.show()


#print(regression)
