#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df1=pd.read_csv("smokers.csv")


# In[3]:


df2=pd.read_csv("fatalities.csv")


# In[4]:


df1.head()


# In[5]:


df2.head()


# ## Handling Missing Data

# In[6]:


df1.isnull().sum()


# In[7]:


df2.isnull().sum()


# In[8]:


df1.dropna(inplace=True)
df2.dropna(inplace=True)


# ## Statistical Summary

# In[9]:


df1.describe()


# In[10]:


df2.describe()


# # Visualization

# Smoking Prevalence Over Time:

# In[11]:


import matplotlib.pyplot as plt

# Define the age groups to plot
age_groups = ['16 and Over', '16-24', '25-34', '35-49', '50-59', '60 and Over']

# Plot smoking trends over time by age group
plt.figure(figsize=(10, 6))
for group in age_groups:
    plt.plot(df1['Year'], df1[group], label=group)

plt.title("Smoking Rates Over Time by Age Group")
plt.xlabel("Year")
plt.ylabel("Smoking Rate (%)")
plt.legend()
plt.grid(True)
plt.show()


# Fatalities Over Time

# In[12]:


# Plot fatalities over time
plt.figure(figsize=(10, 6))
plt.plot(df2['Year'], df2['Value'], color='r', label='Fatalities')
plt.title("Fatalities Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.legend()
plt.grid(True)
plt.show()


# Box Plot: Distribution of Smoking Rates:

# In[13]:


# Convert 'Year' columns to the same data type if needed
df1['Year'] = df1['Year'].astype(str)
df2['Year'] = df2['Year'].astype(str)


# Merge the datasets on 'Year'
merged_data = pd.merge(df1, df2, on='Year', how='inner')



# In[14]:


# Box plot for smoking rates by age group


import seaborn as sns


plt.figure(figsize=(10, 6))
sns.boxplot(data=merged_data[age_groups])
plt.title("Distribution of Smoking Rates by Age Group")
plt.ylabel("Smoking Rate (%)")
plt.show()



# # Correlation Analysis Between Smoking and Fatalities

# In[15]:


# Correlation analysis
correlation = merged_data.corr()
print("Correlation Matrix:\n", correlation)

# Visualizing the correlation matrix using a heatmap
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Between Smoking Rates and Smoking-Related Fatalities")
plt.show()



# In[ ]:




