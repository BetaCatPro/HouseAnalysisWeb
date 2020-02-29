# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

# engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house_info')
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/csv2sql')


"""
import pymysql
conn=pymysql.connect('localhost',port=3306,user='root',passwd=123,db='test')
cursor=conn.cursor()
cursor.execute(sql)
result=cursor.fetchall()   
cursor.close()
conn.close()
res = pd.DataFrame(list(result))

据量很小的情况下
import pandas as pd
import pymysql
conn=pymysql.connect('localhost',port=3306,user='root',passwd='test',db='test')
result=pd.read_sql(sql,conn)
#或者
result=pd.read_sql_query(sql,conn)
"""

df = pd.read_csv("E:\Graduation Project\DataAnalysis\data\jianyang_house.csv", sep=',')
release_data = df['release_date']
import time
# tmp_time = time.strptime(release_data,'%Y年%月m%d日')
# tmp_time = time.strptime('2019年2月10日','%Y年%m月%d日')
# year = str(tmp_time.tm_year)
# month = str(tmp_time.tm_mon)
# day = str(tmp_time.tm_mday)
# final_time = year+'-'+month+'-'+day
# print(final_time)

# 将新建的DataFrame储存为MySQL中的数据表，不储存index列
df.to_sql('house_api', engine, index= False)

print("Write to MySQL successfully!")