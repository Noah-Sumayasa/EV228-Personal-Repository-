# EV228-Personal-Repository-
Personal repository of all EV228 code
Generative AI was not used in this code.
How to operate "func_process_data":
1.) Input the file path first (path + file) then add a comma after
2.) Then add the title of one column of the the data from the file 
3.) Then add the title of a econd column of data from the file 
4.) to display the data parsed, assign function to a variable and print variable


**EV228-Individual-Project**
Generative AI was not used in this code.

Project summary: My project takes two sets of data from the ERA5 detabase, parsing for both the large-scale snowfall and two-meter tempurature, then graphs it on a map that represents Central and Eastern Asia. The map shows both the plot of the data and the boarder of the continent as well as the different boarders of the countries.

Process to generate figures: The data, from the two datasets, was imported and parsed for "longitude", "latitude", "Two meter tempurature", large-scale snowfall", and "valid time". Then, using descriptive statistics, the data of choice could then be used for spatial analysis. Then, the max and min was found for both the latitude and longitude in order to determine the boundries of the plot. Afterwards, using basemap, I created the map features including boundries, continent boarders, and country boarders. Then, I plotted the data by first converting the latitude and longitude data arrays into "mesgrids" then assigning the new latitude and longitude values to x and y coordinates. Then, with those coordinates, I was able to plot it directly onto the generated basemap. Additionally, I added a title, colorbar, colorbar label, and a way to save the figure locally. 

Index of code: fnc_process_data: has the import process_grid_data() which imports and parses for the desired data from the dataset - also has the import basemap_grid_plot() which takes a longitude value, latitude value, the data observed, the validtime, as well as other string inputs that dictate the graphs appearance. Individual_Project: plots Era5 data on a basemap graph using coordinates. 
