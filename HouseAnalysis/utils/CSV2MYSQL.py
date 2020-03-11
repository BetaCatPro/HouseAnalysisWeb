# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')

df = pd.read_csv("E:\\Graduation Project\\DataAnalysis\\housedata\\fin_house2.csv", sep=',',encoding='gbk')

count = 0
l=0
r = 1000
df.iloc[l:r,:].to_sql('house_api', engine, if_exists='append', index=False)
len = df.shape[0]
while len-r > 1000:
    l = l+1001
    r = r+1001
    df.iloc[l:r,:].to_sql('house_api', engine, if_exists='append', index=False)
    print('insert success{} to {}'.format(l,r))
if len-r >0:
    df.iloc[r+1:len, :].to_sql('house_api', engine, if_exists='append', index=False)

print("Write to MySQL successfully!")