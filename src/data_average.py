import pandas as pd
import matplotlib.pyplot as plt

def avg_daily_AQI(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv('../data/AQI/aqi'+str({}).format(year)+'.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

if __name__=="__main__":
    for year in range(2013,2019):
        print('year:', year)
        lst=avg_daily_AQI(year)
        plt.plot(range(0,len(lst)),lst,label=str(year)+ ' data')
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()

