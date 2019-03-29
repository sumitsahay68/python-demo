import pandas as pd

weather_data = {
        'day' : ['1/3/2019','2/3/2019','3/3/2019','5/3/2019','4/3/2019','6/3/2019','7/3/2019','8/3/2019'],
        'temperature' : [25,32,29,35,33,26,28,24],
        'windspeed' : [4,9,6,8,3,6,12,8],
        'event':['sunny','cloudy','rainy','thunderstorm','cloudy','sunny','sunny','clear']
    }


df = pd.DataFrame(weather_data)
print(df)
rows, columns = df.shape
print("Rows: ",rows,"\nColumns: ",columns)
print(df.temperature)  #or df['temperature']
print(df[['event','day']])
print("==========================")
print(df.head(3)) #default arg = 5
print(df.tail()) #default arg = 5
print("----------------------------------------------------")
print(df.head()[['day','temperature']])
print(df.min()[['temperature']])
print(df.min()[['event']])
print(df.mean()[['temperature']])

