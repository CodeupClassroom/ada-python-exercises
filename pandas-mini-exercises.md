# Pandas Exercises

These exercises are intended to be smaller, drill-style exercises. They are
intended to break up the pandas lesson in to smaller chunks.

## Basics

1. Import pandas and numpy

1. Use the code below to generate a data frame for students

    Your data frame should include the student number, student name, shoe_size,
    and favorite number.

    Store your data frame in a variable named `students`

    ```python
    students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
                'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

    student_number = list(range(1, len(students) + 1))
    shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
    side_of_classroom = np.random.choice(['left', 'right'], len(students))
    favorite_number = np.random.randint(1, 11, len(students))
    ```

1. Print out the shape of the data frame.
1. Print out the names of the columns in the data frame.
1. Rename 2 of the columns in your data frame.
1. Create a new data frame based on the one you have. The new data frame should
   only have columns for shoe size and side of the classroom.
1. Create a new data frame that has all of the columns, but only 5 rows.
1. Create a new data frame that has only columns for favorite number and name,
   and only includes 7 rows.
1. Create a new column for the ratio of shoe size to the favorite number. Name
   this `ss_to_fn`
1. Create a new column that contains the z-score for the shoe size.
1. Transform the `side_of_the_classroom` columns such that the values are either
   `R` or `L`.
1. Find the names of all the students that have a shoe size greater than the 3rd
   quartile of shoe sizes (You can use the `.quantile` method on a series for
   this)
1. Find the names of all the students that have a shoe size less than the 1st
   quartile of shoe sizes

## Aggregation & Plotting

1. Calculate the mean, median, min, and max for the shoe sizes and favorite
   numbers
1. Sort the data frame by the students shoe size
1. Sort the data frame by the side of the classroom, then by their student
   number
1. Find the number of students on each side of the classroom
1. Find the average shoe size for each side of the classroom
1. Find the maximum favorite number for each side of the classroom
1. Create a pie chart that visualizes the number of students on each side of the
   classroom.
1. Create a histogram of the shoe sizes in the classroom
1. Create a histogram of the favorite numbers in the classroom
1. Create a scatter plot of shoe size vs favorite number

## Reading & Writing Data

1. Save the students data to a csv file.
1. Read the data from the csv file back into pandas. What do you notice?
1. Create a data frame based on the `profiles.json` file. Explore this data
   frame's structure
1. Write the code necessary to create a data frame based on the results of a SQL
   query to the `numbers` database.
