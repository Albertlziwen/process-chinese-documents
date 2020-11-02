# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:32:05 2020

@author: Albert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
hdtop=pd.read_csv('C:\\Users\\Albert\\Desktop\\hdtop.csv',encoding='ISO-8859-1',sep=',', header=0)

n=1825
count=np.zeros(5)
g=np.zeros(5)
def cal(a,b,c):
    y=2000
    day=(a-y)*365+b*30+c
    return day

for i in range(n):
    for j in range(i,n):
         time1=hdtop["review_date"][i].split("/")
         time2=hdtop["review_date"][j].split("/")
         a1=int(time1[0])
         b1=int(time1[1])
         c1=int(time1[2])
         a2=int(time2[0])
         b2=int(time2[1])
         c2=int(time2[2])
         if cal(a2,b2,c2)-cal(a1,b1,c1)>7:
             if hdtop["star_rating"][i]==1:
                 count[0]+=1
                 g[0]+=j-i
             elif hdtop["star_rating"][i]==2:
                 count[1]+=1
                 g[1]+=j-i
             if hdtop["star_rating"][i]==3:
                 count[2]+=1
                 g[2]+=j-i
             if hdtop["star_rating"][i]==4:
                 count[3]+=1
                 g[3]+=j-i
             if hdtop["star_rating"][i]==5:
                 count[4]+=1
                 g[4]+=j-i
             break
start=hdtop["review_date"][0].split("/")
end=hdtop["review_date"][n-1].split("/")

total_day=cal(int(end[0]),int(end[1]),int(end[2]))-cal(int(start[0]),int(start[1]),int(start[2]))
                
av=n/total_day
sp=g/count/7
print(av)
print(sp)