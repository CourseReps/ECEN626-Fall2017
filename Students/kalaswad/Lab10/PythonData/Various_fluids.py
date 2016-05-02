import numpy as np
import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []      #frequency
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []


##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Acetone.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['frequency']))
        y1.append(float(row['acetone']))
        y2.append(float(row['DI water']))
        y3.append(float(row['ethylene glycol']))
        y4.append(float(row['glass cleaner']))
        y5.append(float(row['hydrocal']))
        y6.append(float(row['isopropyl']))
        y7.append(float(row['pine sol']))
        y8.append(float(row['silicone fluid']))
        y9.append(float(row['simple green']))
        y10.append(float(row['WD 40']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, 'b', label="Acetone") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(x, y2, 'g', label="DI water")
ax1.plot(x, y3, 'k', label="Ethylene glycol")
ax1.plot(x, y4, 'c', label="Glass cleaner")
ax1.plot(x, y5, 'm', label="Hydrocal")
ax1.plot(x, y6, 'y', label="Isopropyl")
ax1.plot(x, y7, 'r', label="Pine sol")
ax1.plot(x, y8, 'b--', label="Silicone fluid")
ax1.plot(x, y9, 'g--', label="Simple green")
ax1.plot(x, y10, 'r--', label="WD 40")

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=5) #add legend at location #1 (top-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Dielectric constant of various fluids') #add plot title
plt.xlabel('Frequency [Hz]') #add x-axis title
plt.ylabel('Dielectric constant') #add y-axis title

plt.show() #required to display plots