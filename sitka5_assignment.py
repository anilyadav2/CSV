import csv
from datetime import datetime
import matplotlib.pyplot as plt



def get_data(a):
    open_file=open(a,'r')
    csv_file=csv.reader(open_file,delimiter=",")
    header_row=next(csv_file)

#deciding indexing for high,low,dates
    
    index_max,index_min,index_date=get_index(header_row)
    high=[]
    date1=[]
    low=[]


    for row in csv_file:
        try:
            int((row[index_max]))
            int((row[index_min]))
            the_date=datetime.strptime(row[index_date],'%Y-%m-%d')
        except:
            print(f"missing data for {the_date}")
        else:
            high.append(row[index_max])
            low.append(row[index_min])
            date1.append(datetime.strptime(row[index_date],'%Y-%m-%d'))

    return high,date1,low





def get_index(header_row):
    for index,column in enumerate(header_row):
        if 'TMAX' in column:
            a=index
        elif 'TMIN' in column:
            b=index
        elif 'DATE' in column:
            c=index
    return(a,b,c)





def subplot(row,station_name,csv_name):
    temp1,date1,temp2=get_data(csv_name)
    plt.subplot(2,1,row)
    plt.title(station_name,fontsize=16)
    plt.ylabel("Temperature in (F)",fontsize=12)
    plt.tick_params(axis='both',which='major',labelsize=12)
    plt.plot(date1,temp1,c='r',alpha=.5)
    plt.plot(date1,temp2,c='b',alpha=.5)
    plt.fill_between(date1,temp1,temp2,facecolor='blue',alpha=.1)
    return plt




def main(Stns):
    tilte1='Temperature comparison between'
    for i in range(len(Stns)):
        subplot(i+1,Stns[i][0],Stns[i][1])
        title1=tilte1+ ' and ' + Stns[i][0]
    plt.suptitle(title1,fontsize=16)
    plt.show()





Stations=[['Sitka Airport, AK US','sitka_weather_2018_simple.csv'],['Sitka Airport, AK US','sitka_weather_2018_simple.csv']]


main(Stations)




