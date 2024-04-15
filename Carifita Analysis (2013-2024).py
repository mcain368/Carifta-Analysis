#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd
import numpy as np 
import os
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns 


# In[136]:


C13 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2013.xlsx")
C14 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2014.xlsx")
C15 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2015.xlsx")
C16 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2016.xlsx")
C17 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2017.xlsx")
C18 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2018.xlsx")
C19 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2019.xlsx")
C22 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2022.xlsx")
C23 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2023.xlsx")
C24 = pd.read_excel(r"C:\Users\mmich\Carifta\Carifta2024.xlsx")


# In[137]:


C13['year'] = 2013
C14['year'] = 2014
C15['year'] = 2015
C16['year'] = 2016
C17['year'] = 2017
C18['year'] = 2018
C19['year'] = 2019
C22['year'] = 2022
C23['year'] = 2023
C24['year'] = 2024


# In[138]:


C13


# In[139]:


combined_data = pd.concat([C13, C14, C15, C16, C17, C18, C19, C22, C23, C24], ignore_index=True)


# In[140]:


combined_data.isnull().sum


# In[141]:


yearly_medal_counts = combined_data.groupby('year')[['Gold', 'Silver', 'Bronze']].sum()

yearly_medal_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Medal Distribution Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)
plt.legend(title='Medal Type')
plt.tight_layout()


# In[142]:


combined_data.columns


# In[143]:


combined_data['Total'] = combined_data['Gold'] + combined_data['Silver'] + combined_data['Bronze']

medals_by_nation_year = combined_data.groupby(['year', 'Nation'])[['Gold', 'Silver', 'Bronze', 'Total']].sum()

medals_by_nation_year.reset_index(inplace=True)

top_performing_nations = medals_by_nation_year.loc[medals_by_nation_year.groupby('year')['Total'].idxmax()]

print(top_performing_nations)

plt.figure(figsize=(10, 6))
for nation in top_performing_nations['Nation'].unique():
    nation_data = top_performing_nations[top_performing_nations['Nation'] == nation]
    plt.plot(nation_data['year'], nation_data['Total'], marker='o', label=nation)

plt.title('Top Performing Nations Each Year')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.legend(title='Nation', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()


# In[144]:


plt.figure(figsize=(10, 6))
combined_data.groupby('year')['Total'].sum().plot(kind='line', marker='o')
plt.title('Total Medals Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.grid(True)
plt.show()


# In[146]:


combined_data


# In[149]:


nations_to_compare = ['Jamaica', 'Bahamas', 'Trinidad and Tobago']
plt.figure(figsize=(10, 6))
for nation in nations_to_compare:
    nation_data = combined_data[combined_data['Nation'] == nation]
    plt.plot(nation_data['year'], nation_data['Total'], label=nation, marker='o')
plt.title('Yearly Medal Counts Comparison')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.legend()
plt.grid(True)
plt.show()


# In[150]:


correlation_matrix = combined_data[['Rank', 'Total', 'Gold']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


# In[152]:


data_2024 = combined_data[combined_data['year'] == 2024]


# In[153]:


data_2024


# In[157]:


medals_2024 = data_2024.groupby('Nation')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
medals_2024.plot(kind='bar', color='skyblue')
plt.title('Performance of Nations in 2024')
plt.xlabel('Nation')
plt.ylabel('Total Medals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[159]:


medal_distribution_2024 = data_2024.groupby('Nation')[['Gold', 'Silver', 'Bronze']].sum()

ax = medal_distribution_2024.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.title('Medal Distribution in 2024')
plt.xlabel('Nation')
plt.ylabel('Total Medals')
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_tick_params(rotation=45, ha='right', pad=5)  
plt.tight_layout()
plt.show()


# In[ ]:




