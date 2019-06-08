# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:20:00 2019

@author: Dell
"""
"""To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?"""




import pandas as pd
df = pd.read_csv("Telecom_churn.csv")
#(1)
new_df = df[(df['international plan']=='yes') & (df['voice mail plan']=='yes')]
print(len(new_df))

#(2)
df_intl = df['total intl minutes']


import pandas as pd


# Loading file
churn_df = pd.read_csv("Telecom_churn.csv")

churned_df = churn_df[churn_df['churn'] == True]
#1
plans_count = churned_df[(churned_df['international plan'] == 'yes') & (churned_df['voice mail plan'] == 'yes')].shape
plans_count = plans_count[0]
print (plans_count)
    

# 2
call_charge = churn_df.groupby('churn')['total intl charge'].sum()
visual_1 = call_charge.plot.pie(autopct='%1.1f%%')

# 3
night_call = churned_df['total night minutes'].max()

# 4
call_analysis = churned_df.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()

# 5
non_churn_al = churn_df['account length'][churn_df['churn'] == False].max()
churn_al = churned_df['account length'].max()
if churn_al > non_churn_al:
    print('churned user have the maximum account lenght')
else:
    print('regular user have the maximum account lenght')

# 6
customer_care = churned_df['customer service calls'].value_counts()

# 7
area_popl = churn_df.groupby('area code')['international plan'].value_counts().unstack()