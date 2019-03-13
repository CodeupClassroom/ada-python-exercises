# IPython log file


import pandas as pd
import numpy as np
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
students
student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))
pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df
students = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
students
type(students)
students.shape
students.columns
students.favorite_number
students
students.rename(columns={'student_no': 'id', 'name': 'student_name'})
students.rename(columns={'student_no': 'id', 'name': 'student_name'},
    inplace=True)
studens.shape
students.shape
students.rename
students
students[['shoe_size', 'side']]
just_shoes_and_sides = students[['shoe_size', 'side']]
students[['shoe_size', 'side']]
students[['side', 'shoe_size']]
students['side', 'shoe_size']
students[['side', 'shoe_size']]
type(students[['side', 'shoe_size']])
type(students[['side']])
type(students['side'])
students.head()
students.sample(5)
students.tail()
students[['favorite_number', 'name']]
students[['favorite_number', 'student_name']]
students[['favorite_number', 'student_name']].head()
students[['favorite_number', 'student_name']].sample(7)
names_and_numbers = students[['favorite_number', 'student_name']]
names_and_numbers.sample(7) 
# students[['favorite_number', 'student_name']].sample(7)
students.sample(7)[['favorite_number', 'student_name']]
students.sample(7)[['favorite_number', 'student_name']][['student_name', 'favorite_number']].head(3)
students.shoe_size
students.favorite_number
students.shoe_size / students.favorite_number
df['ss_to_fn'] = students.shoe_size / students.favorite_number
df
df
del df['ss_to_fn']
df
df
df.drop(columns=['name', 'student_no', 'shoe_size'])
df
df.assign(ss_to_fn=students.shoe_size / students.favorite_number)
df.assign(ss_to_fn=students.shoe_size / students.favorite_number).assign(ss_to_fn=students.shoe_size / students.favorite_number)
df.assign(favorite_number=df.favorite_number + 1)
(df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df['z_shoe_size'] = (df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df
df['z_shoe_size'] = [1, 2, 3]
df['z_shoe_size'] = (df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df.side
df.side.str[0]
df.side.str[0].str.upper()
df.side.apply(lambda side: side[0].upper())
df.shoe_size.quantile
df.shoe_size.quantile(0.25)
df.shoe_size < df.shoe_size.quantile(0.25)
df[df.shoe_size < df.shoe_size.quantile(0.25)]
df[df.shoe_size > df.shoe_size.quantile(0.75)]
get_ipython().system('git status')
