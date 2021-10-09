import csv
from datetime import datetime
open_file=open('sitka_weather_07-2018_simple.csv','r')
csv_file=csv.reader(open_file,delimiter=",")
header_row=next(csv_file)
for index,column in enumerate(header_row):
    print(index,column)

high=[]

for row in csv_file:
    high.append(row[5])

import matplotlib.pyplot as plt


plt.title("weather july",fontsize=16)
plt.xlabel(" ",fontsize=12)
plt.ylabel("Temperature",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.plot(high,c='r',alpha=.5)

plt.show()






