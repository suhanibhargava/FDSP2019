# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:04:57 2019

@author: Dell
"""

Q3. """Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv")

country = dataset['Country'].dropna()
count_country = country.value_counts() 
plt.pie(count_country.values[:10], labels=count_country.index[:10],
autopct='%1.1f%%', shadow=True, startangle=0)
plt.axis('equal')
plt.show()

dataset['Classification'].dropna()value_counts()[:2].plot.bar()


dataset['Artist Display Name'].dropna().value_counts()[:10].plot.bar()

dataset['Culture'].dropna().value_counts()[:2].plot.bar()

