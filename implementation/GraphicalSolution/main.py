#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import gmaps
import gmaps.datasets
from IPython.display import display

# In[2]:


locations = pd.read_csv("data2.csv", sep=";")

# In[3]:


Lon = np.arange(-176.7, 171.7, 0.3484)
Lat = np.arange(5, 71, 0.066)

# In[4]:

# This part refers to the K-Anonymity since it divided the map into 1000x1000 squares
counts = np.zeros((1000, 1000))
for a in range(len(locations)):
    curLat = float((locations['lat'].values[a]).replace(',', '.'))
    curLon = float((locations['long'].values[a]).replace(',', '.'))

    # This is where we add noise to the locations
    noiseLat = np.random.uniform(curLat - 0.2, curLat + 0.2)
    noiseLon = np.random.uniform(curLon - 0.2, curLon + 0.2)

    for b1 in range(1000):
        if Lat[b1] - 0.033 <= noiseLat < Lat[b1] + 0.033:
            for b2 in range(1000):
                if Lon[b2] - 0.1742 <= noiseLon < Lon[b2] + 0.1742:
                    counts[b1, b2] += 1

# In[5]:


gmaps.configure(api_key="AIzaSyBfj7JXQcjBmhhsPY0b0Au23R9hcPILBYw")

# In[6]:


longitude_values = [Lon, ] * 1000
latitude_values = np.repeat(Lat, 1000)
counts.resize((1000000,), refcheck=False)

# In[7]:


heatmap_data = {'Counts': counts, 'latitude': latitude_values, 'longitude': np.concatenate(longitude_values)}
df = pd.DataFrame(data=heatmap_data)

# In[8]:


locations = df[['latitude', 'longitude']]
weights = df['Counts']
fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(locations, weights=weights)
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
display(fig)

# In[ ]:




