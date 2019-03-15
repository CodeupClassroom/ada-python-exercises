# IPython log file


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
tips
# plot the bill amount vs the tip amount based on time of day
get_ipython().run_line_magic('matplotlib', 'qt')
plt.scatter(tips.total_bill, tips.tip)
total_bill_dinner = tips[tips.time == 'Dinner']
tips[tips.time == 'Dinner']
dinner = tips[tips.time == 'Dinner']
lunch = tips[tips.time == 'Lunch']
plt.scatter(dinner.total_bill, dinner.tip)
plt.scatter(dinner.total_bill, dinner.tip)
plt.scatter(lunch.total_bill, lunch.tip)
plt.scatter(dinner.total_bill, dinner.tip, c='red', label='Dinner')
plt.scatter(lunch.total_bill, lunch.tip, c='blue', label='Lunch')
plt.legend()
sns.relplot(data=tips, x='total_bill', y='tip', hue='time')
tips
tips.head()
sns.relplot(data=tips, x='total_bill', y='tip', hue='time', style='smoker')
plt.title('Total Bill vs Tip Amount')
tips.head()
sns.relplot(data=tips, y='tip', x='total_bill', hue='size')
sns.relplot(data=tips, y='tip', x='total_bill', hue='size', style='time')
sns.relplot(data=tips, y='tip', x='total_bill', hue='size', style='time', col='smoker')
sns.relplot(data=tips, y='tip', x='total_bill', style='size')
get_ipython().run_line_magic('pinfo', 'sns.relplot')
tips[['total_bill', 'tip']]
tips[['total_bill', 'tip']].corr()
from pydataset import data
data('mpg')
cars
cars = data('mpg')
cars.head()
cars.corr()
from matplotlib import cm
sns.heatmap(cars.corr(), cmap=cm.PiYG, annot=True, center=0)
sns.heatmap(cars.corr(), cmap=cm.PiYG, annot=True, center=0)
cm.PiYG
from matplotlib import cm
sns.heatmap(cars.corr(), cmap=cm.Blues, annot=True, center=0)
sns.heatmap(cars.corr(), cmap=cm.Blues, annot=True, center=0)
sns.distplot(cars.hwy)
sns.boxplot(data=tips, y='tip')
sns.boxplot(data=tips, y='tip', x='time')
sns.boxplot(data=tips, y='time', x='tip')
sns.boxplot(data=tips, y='time', x='tip', hue='smoker')
sns.pairplot(cars)
sns.violinplot(data=tips, y='time', x='tip')
sns.jointplot(data=tips, y='total_bill', x='tip')
get_ipython().run_line_magic('pinfo', 'sns.jointplot')
sns.relplot(data=tips, y='tip', x='total_bill', style='size')
sns.relplot(data=tips, y='tip', x='total_bill', hue='size')
sns.relplot(data=tips, y='tip', x='total_bill', hue='time')
sns.relplot(data=tips, y='tip', x='total_bill', hue='size', cmap=cm.Blues)
sns.relplot(data=tips, y='tip', x='total_bill', hue='size', cmap=cm.Blues)
