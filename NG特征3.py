#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
from matplotlib import pyplot as plt


# In[106]:


df = pd.read_excel(r'C:\Users\zhou.tianhong\Desktop\2022.02.24.01-02.xlsx')
rows = df.shape[0] - 1
lst = [0 for index in range(df.shape[1])]
lst[0] = 1
df.loc[rows] = lst
df.tail()


# In[107]:


start = 0
sum_info = {}
for x in range(start, rows):        
    if int(df.loc[x, '扭矩 (N·m)']) == int(df.loc[x, '最大扭矩 (N·m)']):
        key = str(df.loc[x, '结果 ID']) + ' ID'
        sum_info[key] = df.loc[x, 'ID']  


# In[113]:


start = 0
outlier = []
max_torque = 0
max_angle = 0
result = {}
for x in range(start, rows):    
    if (int(df.loc[x, 'ID']) < sum_info[str(df.loc[x, '结果 ID']) + ' ID']):
        if float(df.loc[x, '扭矩 (N·m)']) > max_torque:
            max_angle = int(df.loc[x, '角度 (度)'])
        if int(df.loc[x, 'ID'] % 120) == 0:
            outlier.append(max_angle)
            max = 0
            
    if (df.loc[x, '结果 ID'] != df.loc[x + 1, '结果 ID']):
        result[str(df.loc[x, '结果 ID'])] = outlier
        outlier = []
        max_torque = 0
        start = x + 1


# In[114]:


print(result)


# In[ ]:




