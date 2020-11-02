#!/usr/bin/env python
# coding: utf-8

# ### Importing the libraries

# In[54]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Importing the dataset

# In[55]:


covid_death_dataset = pd.read_csv("covid19_deaths_dataset.csv")


# In[56]:


covid_death_dataset.head(10)
covid_death_dataset.shape


# In[57]:


covid_death_dataset.head(10)


# In[58]:


del_col = ["Lat","Long"]


# In[59]:


covid_death_dataset.drop(del_col, axis = 1,inplace=True)


# In[60]:


covid_death_dataset.head(10)


# In[61]:


death_aggregation = covid_death_dataset.groupby("Country/Region").sum()


# In[62]:


death_aggregation.head(10)


# ### Analyze the death rate for India and china

# In[63]:


death_aggregation.loc["India"].plot()
death_aggregation.loc["China"].plot()
plt.legend()


# In[64]:


countries = list(death_aggregation.index)
max_death_rate = []
for i in countries:
    max_death_rate.append(death_aggregation.loc[i].diff().max())
death_aggregation["max_death_rate"] = max_death_rate


# In[65]:


death_aggregation.head(10)


# In[66]:


death_data = pd.DataFrame(death_aggregation["max_death_rate"])


# In[67]:


death_data.head(10)


# ### Importing hapiness dataset

# In[68]:


hapiness_data = pd.read_csv("worldwide_happiness_report.csv")


# In[69]:


hapiness_data.head(10)


# In[70]:


col_to_drop = ["Overall rank", "Score","Generosity","Perceptions of corruption"]


# In[71]:


hapiness_data.drop(col_to_drop,axis=1,inplace=True)
hapiness_data.head(10)


# In[72]:


new_df = hapiness_data.set_index("Country or region")


# # # Joining the hapiness data set and death dataset

# In[73]:


dea_happ_data = new_df.join(death_data,how='inner')


# In[74]:


new_df.head(10)


# ### Finding the corelation

# In[75]:


dea_happ_data.corr()


# In[76]:


dea_happ_data.head(10)


# ## Visualizing

# ### visualizing GDP per  capita vs  max_death_rate

# In[77]:


x = dea_happ_data['GDP per capita']
y = dea_happ_data['max_death_rate']
sns.scatterplot(x,np.log(1+y))


# In[78]:


sns.regplot(x, np.log(1+y))


# ### visualizing Social Support vs max_death_rate

# In[79]:


x = dea_happ_data['Social support']
y = dea_happ_data['max_death_rate']
sns.scatterplot(x,np.log(1+y))


# In[80]:


sns.regplot(x, np.log(1+y))


# ### visualizing Healthy life expectancy	 vs max_death_rate

# In[81]:


x = dea_happ_data['Healthy life expectancy']
y = dea_happ_data['max_death_rate']
sns.scatterplot(x,np.log(1+y))


# In[82]:


sns.regplot(x, np.log(1+y))


# ### Visualizing Freedom to make life choices vs max_death_rate

# In[83]:


x = dea_happ_data['Freedom to make life choices']
y = dea_happ_data['max_death_rate']
sns.scatterplot(x,np.log(1+y))


# In[84]:


sns.regplot(x, np.log(1+y))


# # Importing covid confirmed dataset

# In[85]:


cases = pd.read_csv('covid19_Confirmed_dataset.csv')


# In[86]:


cases.head(10)


# In[87]:


cases.drop(["Lat","Long"], axis = 1, inplace =True)
cases.head(10)


# In[88]:


new_cases_df = cases.groupby('Country/Region').sum()
new_cases_df.head(10)


# In[89]:


new_cases_df.head(10)


# In[90]:


countries = list(new_cases_df.index)
max_confirmed_rate = []
for i in countries:
    max_confirmed_rate.append(new_cases_df.loc[i].diff().max())
new_cases_df["max_confirmed_rate"] = max_confirmed_rate


# In[91]:


new_cases_df.head(10)


# In[92]:


dea_happ_data.head(1)


# In[93]:


new_cases_df=new_cases_df.join(dea_happ_data,how='inner')
new_cases_df.head(10)


# In[99]:


new_df = new_cases_df.iloc[:,-6:-1]
new_df['max_death_rate'] = new_cases_df['max_death_rate']
new_df.head(10)


# ### Correlation

# In[100]:


new_df.corr()


# ### Visualizing

# ### visualizing max_confirm_rate vs GDP per capita

# In[108]:


y = new_df['max_confirmed_rate']
x = new_df['GDP per capita']
sns.scatterplot(x,np.log(y))


# In[109]:


sns.regplot(x,np.log(y))


# ### visualizing max_confirm_rate vs Freedom to make life choices

# In[110]:


y = new_df['max_confirmed_rate']
x = new_df['Freedom to make life choices']
sns.scatterplot(x,np.log(y))


# In[112]:


sns.regplot(x,np.log(y))


# #### visualizing max_confirm_rate vs max_death_rate

# In[101]:


x = new_df['max_confirmed_rate']
y = new_df['max_death_rate']


# In[104]:


sns.scatterplot(np.log(1+x),np.log(1+y))


# In[105]:


sns.regplot(np.log(1+x),np.log(1+y))


# In[ ]:




