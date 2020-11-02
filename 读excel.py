# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:05:21 2020


@author: Albert
"""
import numpy as np
import pandas as pd
'''
data = pd.read_excel("C:\\Users\\Albert\\Desktop\\WORK\\华润\\10.26\\1024各项目编制\\北京橡树湾.xlsx",encoding = 'gbk')

list =['润西山','理想国','悦景湾','万橡悦府','小米','北京橡树湾','下花园','密云橡树湾','海淀北','海淀南']
df=np.zeros((len(list),data.shape[1]))
#命名Dataframe最好不要大写
kk = pd.DataFrame(df)

name = "C:\\Users\\Albert\\Desktop\\WORK\\华润\\10.26\\1024各项目编制\\"
j=0
for i in list:
  data=pd.read_excel(name+i+".xlsx",encoding='gbk')
  #转化成列表比读写Series数据类型更好
  kk.loc[j]= data.loc[data.shape[0]-2][0:45].tolist()
  j = j+1
  
kk.to_csv(name+"汇总"+".csv",encoding='gbk')
'''
name = "C:\\Users\\Albert\\Desktop\\WORK\\华润\\10.26\\1024各项目编制\\"
k='海淀南'
data=pd.read_excel(name+k+".xlsx",encoding='gbk')
data = data.fillna(0)
def find(name):
  sum20_4, sum21_1, sum21_2, sum21_3, sum21_4= 0, 0, 0, 0, 0
  sum20_9 = 0
  t =0
  for i in range(data.shape[0]):
    if name in str(data['Unnamed: 0'][i]):
      #2020年4季度
      t =i+3
      sum20_4 = sum20_4 + data['Unnamed: 15'][t]+ \
      data['Unnamed: 16'][t] + data['Unnamed: 17'][t]
      
      #2021 1季度
      sum21_1 = sum21_1 + data['2021年'][t]+ \
      data['Unnamed: 20'][t] + data['Unnamed: 21'][t]
      
      sum21_2 = sum21_2 + data['Unnamed: 22'][t]+ \
      data['Unnamed: 23'][t] + data['Unnamed: 24'][t]
      
      sum21_3 = sum21_3 + data['Unnamed: 25'][t]+ \
      data['Unnamed: 26'][t] + data['Unnamed: 27'][t]
      
      sum21_4 = sum21_4 + data['Unnamed: 28'][t]+ \
      data['Unnamed: 29'][t] + data['Unnamed: 30'][t]
      
      #2020年前9月合计
      sum20_9 = sum20_9 +data['Unnamed: 14'][t]
      
  return [sum20_4, sum21_1, sum21_2, sum21_3, sum21_4]

print(find('住宅'))
'''   
sum = (0,0,0,0,0)   
for i in range(6):
  t=i+43
  z ="北京润西山-4期|北京润西山4期"+str(t)+"#"

  print(find(z))

for i in range(21):
  t = i+22
  z="-3期|开发-住宅-别墅叠拼-普通-毛坯"+str(t)
  
  print(find(z))
'''
'''
#1.1/1.2
sum = np.zeros(5)
for i in range(21):
  t = i+22
  z = str(t)
  if t not in [27,28,29]:
    sum += np.array(find(z))
 
print(sum)
'''
'''
#2.1
sum = 0
for i in range(6):
  r=i+43
  z =str(r)
  sum+=find(z)
  
print(sum)
'''
'''
#2.2
sum = 0
for i in range(5):
  r=i+49
  z=str(r)
  sum+=find(z)
  
print(sum)
'''