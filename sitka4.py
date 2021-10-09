import csv
from datetime import datetime
import matplotlib.pyplot as plt
open_file=open('death_valley_2018_simple.csv','r')
csv_file=csv.reader(open_file,delimiter=",")
header_row=next(csv_file)


high=[]
date1=[]
low=[]
for row in csv_file:
    try:
        int((row[5]))
        int((row[6]))
        the_date=datetime.strptime(row[2],'%Y-%m-%d')
    except:
        print(f"missing data for {the_date}")
    else:
        high.append(row[5])
        low.append(row[6])
        date1.append(datetime.strptime(row[2],'%Y-%m-%d'))


fig=plt.figure()
plt.subplot(2,1,1)
plt.title("High",fontsize=16)
plt.xlabel(" ",fontsize=12)
plt.ylabel("temperature",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.plot(date1,high,c='r',alpha=.5)

plt.subplot(2,1,2)
plt.title("low",fontsize=16)
plt.xlabel(" ",fontsize=12)
plt.ylabel("Temperature in (F)",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)
plt.plot(date1,low,c='b',alpha=.5)
plt.suptitle("Low and high temperatue",fontsize=16)
plt.show()





