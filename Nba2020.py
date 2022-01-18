#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = '2020'
str = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'

url = str.format(year)
url


# In[5]:


import pandas as pd
df = pd.read_html(url, header = 0)
df


# In[6]:


len(df)


# In[7]:


df[0]


# In[9]:


df2020 = df[0]


# In[10]:


#Cleaning
df2020[df2020.Age == 'Age']


# In[12]:


df = df2020.drop(df2020[df2020.Age == 'Age'].index)


# In[13]:


df.shape


# In[ ]:




