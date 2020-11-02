import numpy as np
import pandas as pd

data2 = pd.read_csv('C:\\Users\\Albert\\Desktop\\2.csv',encoding = 'gbk')
data3 = pd.read_csv('C:\\Users\\Albert\\Desktop\\3.csv',encoding = 'gbk')

data2=data2.fillna(0)
'''
for i in range(1207):
  if data2['202002'][i] == 0:
    data2['202002'][i]=data2['202002'][i-1]
  
'''
#设计三列：月份，产业，钱
data = np.zeros(1740*3).reshape(1740,3) 
df = pd.DataFrame(data)
#日历生成器
def cal(n):
  #起始日期201802
  year = 2018
  month = 2
  smonth=''
  if n+2>12 and n+2<24:
    year = year+1
    month = n+2-11
    if month < 10:
      smonth = '0'+str(month)
    else:
      smonth = str(month)
    
  elif n+2>24 or n+2==24:
    year = year+2
    month = n - 24 + 4
    if month < 10:
      smonth = '0'+str(month)
    else:
      smonth = str(month)
  else:
    month = month+n
    if month < 10:
      smonth = '0'+str(month)
    else:
      smonth = str(month)
        
  return str(year)+smonth
    
for i in range(29):
  df[0][i*60] = cal(i)
  
for i in range(1740):
  if df[0][i] == 0:
    df[0][i]=df[0][i-1]
    
for i in range(1740):
  df[1][i] = data3['1'][i%60]

for i in range(1740):
  for j in range(1208):
    if df[0][i]==data2['0'][j] and df[1][i]==data2['4'][j]:
        df[2][i] = data2['9'][j]
