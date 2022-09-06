#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt


# In[196]:


df = pd.read_excel(r'C:\Users\zhou.tianhong\Desktop\2022.02.24.01-02.xlsx')
rows = df.shape[0] - 1
lst = [0 for index in range(df.shape[1])]
lst[0] = 1
df.loc[rows] = lst
df.tail()


# In[197]:


start = 0
sum_info = {}
for x in range(start, rows):    
    if (df.loc[x, '结果 ID'] != df.loc[x + 1, '结果 ID']):
        key = str(df.loc[x, '结果 ID']) + ' max angle'
        sum_info[key] = df.loc[x, '最大角度 (度)']
        start = x + 1
        
    if int(df.loc[x, '扭矩 (N·m)']) == int(df.loc[x, '最大扭矩 (N·m)']):
        key = str(df.loc[x, '结果 ID']) + ' ID'
        sum_info[key] = df.loc[x, 'ID']    


# In[198]:


start = 0
for x in range(start, rows):    
    if (int(df.loc[x, '扭矩 (N·m)']) < 0.6) & (int(df.loc[x, 'ID']) < sum_info[str(df.loc[x, '结果 ID']) + ' ID']):
        key = str(df.loc[x, '结果 ID']) + ' min angle'
        sum_info[key] = df.loc[x, '角度 (度)']


# In[199]:


angle_diff = {}
start = 0
for x in range(start, rows):  
    if (df.loc[x, '结果 ID'] != df.loc[x + 1, '结果 ID']):
        key = str(df.loc[x, '结果 ID']) + ' max angle'
        max_angle = sum_info[key]
        key = str(df.loc[x, '结果 ID']) + ' min angle'
        min_angle = sum_info[key]
        key = str(df.loc[x, '结果 ID']) + ' difference'
        angle_diff[key] = max_angle - min_angle


# In[200]:


lst_ok = []
lst_ng = []
for key in angle_diff.keys():
    if angle_diff[key] > 70:
        lst_ok.append(int(key.split()[0]))
    else:
        lst_ng.append(int(key.split()[0]))
print(lst_ng)
print(lst_ok)


# In[ ]:




