import csv
from datetime import datetime
open_file=open('sitka_weather_2018_simple.csv','r')
csv_file=csv.reader(open_file,delimiter=",")
header_row=next(csv_file)


high=[]
date1=[]
low=[]
for row in csv_file:
    high.append(row[5])
    low.append(row[6])
    date1.append(datetime.strptime(row[2],'%Y-%m-%d'))

import matplotlib.pyplot as plt


fig=plt.figure()
plt.title("weather july",fontsize=16)
plt.xlabel(" ",fontsize=12)
plt.ylabel("temp",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.plot(date1,high,c='r',alpha=.5)
plt.plot(date1,low,c='blue',alpha=.5)

plt.fill_between(date1,high,low,facecolor='blue',alpha=.1)
fig.autofmt_xdate()
plt.show()




