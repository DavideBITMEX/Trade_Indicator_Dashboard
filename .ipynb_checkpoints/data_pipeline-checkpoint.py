#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

# Step 1: Fetch data from the World Bank API
api_url = "https://api.worldbank.org/v2/country/DE/indicator/NE.EXP.GNFS.KD.ZG?format=json"
response = requests.get(api_url)
data_json = response.json()


# In[3]:


# Step 2: Convert JSON to a DataFrame
data_list = data_json[1]  # The second element usually holds the actual data
df = pd.DataFrame(data_list)
print(df.head())

# Step 3: Clean and transform
df = df[['countryiso3code', 'date', 'value']]
df.dropna(subset=['value'], inplace=True)      # Remove rows with missing values in 'value'
df['value'] = df['value'].astype(float)        # Ensure the column is numeric

print(df.head())


# In[ ]:





# In[ ]:




