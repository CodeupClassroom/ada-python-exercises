import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

print("\n--- How many negative numbers are there?")

print('    {} negative numbers'.format((a < 0).sum()))

print("\n--- How many positive numbers are there?")

print('    {} positive numbers'.format((a > 0).sum()))

print("\n--- How many even positive numbers are there?")
evens = a[a % 2 == 0]
positive_even = evens[evens > 0]
print('    {} positive even numbers'.format(positive_even.shape[0]))

print("\n--- If you were to add 3 to each data point, how many positive numbers would there be?")

b = a + 3

print('    {} positive numbers'.format(b[b > 0].shape[0]))

print("\n--- If you squared each number, what would the new mean and standard deviation be?")

c = a ** 2
print('    new mean: {}'.format(c.mean()))
print('    new standard deviation: {}'.format(c.std()))

print("\n--- A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.")

centered = a - a.mean()
print('    centered data: {}'.format(centered))
print('    centered data mean: {}'.format(centered.mean()))

print("\n--- Calculate the z-score for each data point. Recall that the z-score is given by:")

z_scores = (a - a.mean()) / a.std()
print('    zscores: {}'.format(z_scores.round(2)))

print("\n--- Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.")

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a *= n

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for n in a:
    squares_of_a.append(n ** 2)
## OR
squares_of_a = [n ** 2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for n in a:
    if n % 2 == 1:
        odds_in_a.append(n)
## OR
[n for n in a if n % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)
## OR
[n for n in a if n % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
b.sum()

# Exercise 2 - refactor the following to use numpy.
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max()


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product
# of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
b ** 2

# # Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
b[b % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
b.shape

# Exercise 10 - transpose the array b.
b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing
# only 1 number (6 x 1)
b.reshape((6, 1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.min()
c.max()
c.sum()
c.prod()

# Exercise 2 - Determine the standard deviation of c.
c.std()

# Exercise 3 - Determine the variance of c.
from math import sqrt
sqrt(c.std())

# Exercise 4 - Print out the shape of the array c
c.shape

# Exercise 5 - Transpose c and print out transposed result.
c.T

# Exercise 6 - Multiply c by the c-Transposed and print the result.
c * c.T

# Exercise 7 - Write the code necessary to sum up the result of c times c
# transposed. Answer should be 261
(c * c.T).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c
# transposed. Answer should be 131681894400.
(c * c.T).prod()


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

# Exercise 4 - Find all the negative numbers in d
d[d < 0]

# Exercise 5 - Find all the positive numbers in d
d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).shape[0]

# Exercise 8 - Print out the shape of d.
d.shape

# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape((9, 2))
