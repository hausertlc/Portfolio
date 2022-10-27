#!/usr/bin/env python
# coding: utf-8

# In[11]:


# First let's import the packages we will use in this project
# You can do this all now or as you need them
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

pd.options.mode.chained_assignment = None



# Now we need to read in the data
df = pd.read_csv( r'C:\Users\hause\Downloads\movies.csv.zip')


# In[12]:


# Now let's take a look at the data

df


# In[13]:


# We need to see if we have any missing data
# Let's loop through the data and see if there is anything missing

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[19]:


df = df.dropna()


# In[14]:


# Data Types for our columns

print(df.dtypes)


# In[23]:


df['budget'] =df['budget'].astype('int64')
df['gross'] =df['gross'].astype('int64')


# In[24]:


df


# In[32]:


df['yearcorrect'] = df['released'].str.extract(pat = '([0-9]{4})').astype(int)


# In[33]:


df


# In[34]:


df['yearcorrect']=df['released'].astype(str).str[:4]
df


# In[39]:


df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[38]:


pd.set_option('display.max_rows',None)


# In[ ]:





# In[15]:


# Are there any Outliers?

df.boxplot(column=['gross'])


# In[ ]:





# In[41]:


df.drop_duplicates()

df['company'].drop_duplicates().sort_values(ascending=False)


# In[ ]:





# In[ ]:



# Order our Data a little bit to see

df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[45]:


#looking at scatterplot wit hbudget vs gross revenue
plt.scatter(x=df['budget'], y=df['gross'])
plt.title ('Budet vs Gross Earnings')
plt.xlabel('Budget')
plt.ylabel ('Earnings')
plt.show


# In[53]:


sns.regplot(x="budget", y="gross", data=df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})


# In[55]:


#correlation
df.corr() #pearson is default




# In[57]:


df.corr(method="spearman")


# In[58]:


df.corr(method="kendall")


# In[60]:


# high corr btw budget and gross

correlation_matrix=df.corr(method="pearson")
sns.heatmap(correlation_matrix, annot = True)
plt.title ('Correlation Matrix')
plt.xlabel('Movie Features')
plt.ylabel ('Movie Features')
plt.show


# In[64]:


# look at company
df_numerized = df


for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized


# In[65]:


df_numerized.corr(method='pearson')


# In[66]:


correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[67]:


df_numerized.corr()


# In[68]:


correlation_mat=df_numerized.corr()
corr_pairs=correlation_mat.unstack()
corr_pairs


# In[69]:


sorted_pairs=corr_pairs.sort_values
sorted_pairs


# In[75]:





# In[ ]:




