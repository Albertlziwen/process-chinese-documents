# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:06:32 2020

@author: Albert
"""

'''
for i in range(9644):
    for word in b_hd[i].split():
        if word == 'dryer':
            p=1
            break
        else:
            p=0
    if p==0:
        train2=train2.drop(i)
        p=1
'''
'''
train2.to_csv('C:\\Users\\Albert\\Desktop\\hd6删完数据.csv',sep=',',header=True,index=True)

from textblob import TextBlob
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print (testimonial.sentiment)
'''
'''
#P(H|E)
n=7394
vine_count=0#vine计数
vine_helpful=0
nvine_helpful=0
total_helpful=0
for i in range(88):
    if train2['vine'][i] =="Y":
        vine_helpful = train2['helpful_votes'][i]+vine_helpful
        vine_count += 1
    else:
        nvine_helpful = train2['helpful_votes'][i] + nvine_helpful
    
total_helpful=vine_helpful+nvine_helpful
#PHE=vine_helpful/total_helpful
#P(H)
P_H=vine_count/n
P_E=0.1
#P(E|H)
#PEH=PHE*P_E/P_H
print(P_H)       
'''