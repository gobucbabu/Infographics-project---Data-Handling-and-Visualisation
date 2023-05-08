# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:28:25 2023

@author: gobub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns

df0 = pd.read_csv("mcu_box_office.csv", parse_dates=['release_date'])

df0.sort_values("worldwide_box_office", ascending=False)
dfbarh = df0.head(5).set_index('release_date').sort_index()
plt.figure(0)
ax1 = sns.barplot(data=dfbarh, y='movie_title', x='worldwide_box_office', color='red' ,edgecolor='k', linewidth=1.5)
ax1.set_title('Top 5 highest grossing \n films of the Infinity Saga', fontweight='bold', fontsize='x-large')
ax1.set_ylabel('Movie', fontweight='bold', fontstyle='italic', fontsize='large')
ax1.set_xlabel('Worldwide box office gross\n (Billion USD)', fontstyle='italic', fontweight='bold', fontsize='large')
plt.xticks(rotation=25)
plt.show()


plt.figure(1)
ax2 = sns.relplot(data=df0, x='production_budget', y='worldwide_box_office',
                  hue='mcu_phase', style='mcu_phase', size='mcu_phase', palette=['lightcoral', 'red', 'maroon'])
ax2.set(title='Relational plot between Budget and Box office',
        xlabel='Production Budget \n (Million USD)', ylabel='Box offic gross \n (Billion USD)')
plt.show()

plt.figure(2)
df0['sum'] = df0['audience_score'] + df0['tomato_meter']
dfbar = df0.sort_values('sum', ascending=False).head(8)
ax3 = dfbar.plot( x='movie_title', y=['audience_score', 'tomato_meter'], kind='bar', color=['tomato', 'firebrick'])
ax3.set_title('Top 5 movies with highest combined rating', fontweight='bold', fontsize='x-large')
ax3.set_xlabel('Movie', fontweight='bold', fontstyle='italic', fontsize='large')
ax3.set_ylabel('Rating', fontstyle='italic', fontweight='bold', fontsize='large')
plt.xticks(rotation=85)
plt.show()

plt.figure(3)
ax2 = sns.relplot(data=df0, x='release_date', y='opening_weekend', kind='line', color='firebrick')
ax2.set(title='Change in opening weekend gross over time',
        xlabel='Years', ylabel='Opening weekend gross \n (million USD)')
plt.show()

plt.figure(4)
df0.groupby('mcu_phase').sum().plot(kind='pie', y='worldwide_box_office', colors=['firebrick', 'salmon', 'red'])
plt.show()



