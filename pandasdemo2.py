import pandas as pd

df = pd.read_csv("pandas_tutorial_read.csv",delimiter = ";",names=['date_time','read/write','country','user_id','digital_marketing','continent'])

#print(df)
#print(df[df.digital_marketing=="SEO"])
print(df.head()[['country','continent','user_id']])
print(df.sample(5))   #random pick up
