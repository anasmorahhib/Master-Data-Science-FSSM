#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


# On charge le dataset
house_data_raw = pd.read_csv('house.csv')
house_data = house_data_raw[house_data_raw['loyer'] < 7000]
# On affiche le nuage de points dont on dispose
fig = plt.figure(figsize=(10,8))
plt.plot(house_data['surface'], house_data['loyer'], 'mo', markersize=4)
plt.style.use(plt.style.available[5])
plt.show()


# In[84]:


# On décompose le dataset et on le transforme en matrices pour pouvoir effectuer notre calcul
X = np.matrix([np.ones(house_data.shape[0]), house_data['surface'].values]).T
y = np.matrix(house_data['loyer']).T

# On effectue le calcul exact du paramètre theta
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
print(theta)


# In[100]:


fig = plt.figure(figsize=(10,8))
plt.xlabel('Surface')
plt.ylabel('Loyer')
plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)

# On affiche la droite entre 0 et 250
plt.plot([0,250], [theta.item(0) + 0 * theta.item(1) ,theta.item(0) + 250 * theta.item(1)], linestyle='--', c='#000000')
plt.style.use(plt.style.available[5])
plt.show()


# In[ ]:




