# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:59:01 2019

@author: Dell
"""

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""

import pandas as pd
import numpy as np
from collections import Counter


json_df = pd.read_json("usagov_bitly_data.json",lines = True)
json_df = json_df.replace([np.nan, ""], ["Mising", "Unknown"])    
json_df_tz = json_df['tz'].value_counts().head(10)    
json_tz = Counter(json_df['tz'])
json_tz = sorted(json_tz.items(), key=lambda x: x[1], reverse=True)
json_tz = json_tz[:10] 
tz_count = json_df['tz'].value_counts()
json_df_tz.plot.bar()
tokens_df = json_df['a'].str.split(n=1, expand=True).add_prefix("Token_")
tokens_frequency = tokens_df['Token_0'].value_counts()
tokens_frequency.head().plot.bar()
tokens_df = tokens_df.replace(np.nan, 'Missing value') 
tokens_df["os"] = 'Not Windows'
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"
