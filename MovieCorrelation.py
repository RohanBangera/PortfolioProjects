#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

df = pd.read_csv(r'C:\Users\rohan\Downloads\movies.csv')


# In[4]:


df.head()


# In[5]:


#missing data check

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[6]:


df.dtypes


# In[5]:


df.sort_values(by=['gross'],inplace=False, ascending=False)


# In[15]:


pd.set_option('display.max_rows',None)


# In[16]:


#dropping duplicates
df.drop_duplicates()


# In[22]:


#buget vs gross scatter plot

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Buget vs Gross')
plt.xlabel('Film Budget')
plt.ylabel('Gross Earnings')


# In[23]:


df.head()


# In[28]:


#seaborn plot
sns.regplot(x='budget',y='gross',data=df,scatter_kws={"color":"red"}, line_kws={"color":"blue"})


# In[29]:


df.corr()


# In[31]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix,annot=True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[6]:


df_number =df

for col_name in df_number.columns:
    if(df_number[col_name].dtype == 'object'):
        df_number[col_name] = df_number[col_name].astype('category')
        df_number[col_name] = df_number[col_name].cat.codes

df_number.head()
        
    


# In[36]:


correlation_matrix = df_number.corr(method='pearson')

sns.heatmap(correlation_matrix,annot=True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[37]:


df_number.corr()


# In[38]:


correlation_mat = df_number.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs

    


# In[39]:


sorted_pairs = corr_pairs.sort_values()
sorted_pairs


# In[41]:


high_corr = sorted_pairs[(sorted_pairs) > 0.5]

high_corr


# In[ ]:


#(gross and votes),(gross and budget) have a high correlation

