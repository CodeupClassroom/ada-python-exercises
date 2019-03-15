# IPython log file


import pandas as pd
def get_db_url(user, host, password, db, driver='pymysql'):
    return f'mysql+{driver}://{user}:{password}@{host}/{db}'
    
import env
url = get_db_url(env.username, env.hostname, env.password, db='employees')
from sqlalchemy import create_engine
connection = create_engine(url)
employees = pd.read_sql('SELECT * FROM employees', connection)
employees
titles = pd.read_sql('SELECT * FROM titles', connection)
titles
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
titles.groupby('title').count()
titles.value_counts()
titles.title.value_counts()
titles.title.value_counts().plot()
titles.title.value_counts().plot.bar()
plt.xticks(rotation=30)
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.2)
titles.dtypes
titles.to_date > 3
titles.to_date != '9999-01-01'
(titles.to_date != '9999-01-01').all()
titles.to_date
(titles.to_date != '9999-01-01').all()
from datetime import datetime
datetime.now()
(titles.to_date > datetime.now()).any()
(titles.to_date > datetime.date()).any()
(titles.to_date > datetime.now().date).any()
(titles.to_date > datetime.now().date()).any()
titles.to_date > datetime.now().date()
titles[titles.to_date > datetime.now().date()]
current_titles = titles[titles.to_date > datetime.now().date()]
current_titles.value_counts().plot.bar()
current_titles.title.value_counts().plot.bar()
current_titles.title.value_counts().plot.bar()
# how many titles does each employee have?
titles.emp_no.value_counts()
titles.emp_no.value_counts().value_counts()
titles.emp_no.value_counts().value_counts().plot.bar()
get_ipython().run_line_magic('pinfo', 'employees.join')
employees.join(titles, on='emp_no')
employees.join(titles, on='emp_no', lsuffix='_emp')
employees.join(titles, on='emp_no', lsuffix='_emp', how='right')
employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')
employees_with_titles = employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')
get_ipython().run_line_magic('pinfo', 'employees.merge')
get_ipython().run_line_magic('pinfo', 'employees.join')
employees_with_titles
employees_with_titles.groupby('title')[['hire_date']].max()
url = get_db_url(env.username, env.hostname, env.password, db='chipotle')
connection = create_engine(url)
orders = pd.read_sql('SELECT * FROM orders')
orders = pd.read_sql('SELECT * FROM orders', connection)
orders.head()
orders.head()
orders.dtypes
orders.item_price.replace('')
orders.item_price.replace('$', '')
orders.item_price.str.replace('$', '')
orders.item_price.str.replace('$', '').astype('float')
orders.item_price = orders.item_price.str.replace('$', '').astype('float')
orders.head()
orders[orders.quantity >= 2]
orders[orders.quantity >= 2].head(20)
orders[orders.quantity >= 2].head(20).drop(columns=['choice_description', 'id', 'order_id'])
orders[orders.item_name == 'Canned Soda']
orders[orders.item_name == 'Canned Soda'].choice_description
orders[orders.item_name == 'Canned Soda'].choice_description.value_counts()
orders.groupby('order_id').sum()
orders[['order_id', 'item_price']].groupby('order_id').sum()
order_prices = orders[['order_id', 'item_price']].groupby('order_id').sum()
order_prices.plot.hist()
order_prices.describe()
orders.item_name.value_counts()
orders.item_name.value_counts().head(7)
orders[['item_name', 'item_price']].groupby('item_name').sum()
orders[['item_name', 'item_price']].groupby('item_name').sum().sort_values('item_price')
orders[['item_name', 'item_price']].groupby('item_name').sum().nlargest(7)
orders[['item_name', 'item_price']].groupby('item_name').sum().nlargest(7, 'item_price')
orders.item_name.value_counts().head(7)
