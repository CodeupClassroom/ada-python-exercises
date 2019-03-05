# 1. Conditional Basics
# 1. prompt the user for a day of the week, print out whether the day is Monday
#    or not

weekday = input('Please enter a weekday: ')
print(f'weekday = {weekday}')
if weekday == 'Monday':
    print("Sounds like someone has a case of the Mondays!")
else:
    print('It is not Monday')

# 2. prompt the user for a day of the week, print out whether the day is a
#    weekday or a weekend

weekday = input('Please enter a day of the week: ')
if weekday == 'Saturday' or weekday == 'Sunday':
    print('It is a weekend')
else:
    print('It is a weekday')

weekday = input('Please enter a day of the week: ')
if weekday.lower().startswith('s'):
    print('It is a weekend')
else:
    print('It is a weekday')

weekend_days = ['saturday', 'sunday', 'sat', 'sun']
weekday = input('Enter a weekday: ')
if weekday.lower() in weekend_days:
    print('Weekend!')
else:
    print('Weekday!')

hours_worked = 43
hourly_rate = 900
if hours_worked > 40:
    pay_at_regular_rate = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
    paycheck = pay_at_regular_rate + overtime_pay
else:
    paycheck = hourly_rate * hours_worked

print(paycheck)

# 1. Loop Basics

#     1. While

#         - Create an integer variable `i` with a value of 5.
#         - Create a while loop that runs so long as `i` is less than or equal to
#           15
#         - Each loop iteration, output the current value of `i`, then increment
#           `i` by one.

#         Your output should look like this:

#             5
#             6
#             7
#             8
#             9
#             10
#             11
#             12
#             13
#             14
#             15

i = 5
while i <= 15:
    print(i)
    i += 1

#         - Create a while loop that will count by 2's starting with 0 and ending
#           at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

#         - Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while True:
    print(len(str(i)))
    i = i ** 2

#         - Create a while loop that starts at 2, and displays the number
#           squared on each line while the number is less than 1,000,000. Output
#           should equal:

#             ```
#              2
#              4
#              16
#              256
#              65536
#             ```

i = 2
while i < 1_000_000:
    print(i)
    i *= i
    # same as
    # i = i ** 2

#         1. Write a loop that uses `print` to create the output shown below.

#                 100
#                 95
#                 90
#                 85
#                 80
#                 75
#                 70
#                 65
#                 60
#                 55
#                 50
#                 45
#                 40
#                 35
#                 30
#                 25
#                 20
#                 15
#                 10
#                 5

i = 100
while i >= 5:
    print(i)
    i -= 5

for n in range(100, 0, -5):
    print(n)

#     1. For Loops

#         1. Write some code that prompts the user for a number, then shows a
#            multiplication table up through 10 for that number.

#             For example, if the user enters `7`, your program should output:

#                 7 x 1 = 7
#                 7 x 2 = 14
#                 7 x 3 = 21
#                 7 x 4 = 28
#                 7 x 5 = 35
#                 7 x 6 = 42
#                 7 x 7 = 49
#                 7 x 8 = 56
#                 7 x 9 = 63
#                 7 x 10 = 70

x = int(input('Please enter a number: '))

for n in range(1, 11):
    output = '{} x {} = {}'.format(x, n, x * n)
    print(output)


#         1. Create a `for` loop that uses `print` to create the output shown below.

#                 1
#                 22
#                 333
#                 4444
#                 55555
#                 666666
#                 7777777
#                 88888888
#                 999999999

for n in range(1, 10):
    print(str(n) * n)


#     1. `break` and `continue`

#         1. Prompt the user for an odd number between 1 and 50. Use a loop and a `break`
#            statement to continue prompting the user if they enter invalid input. (Hint:
#            use the `isdigit` method on strings to determine this). Use a loop and the
#            `continue` statement to output all the odd numbers between 1 and 50, except
#            for the number the user entered.

#             Your output should look like this:

#                 Number to skip is: 27

#                 Here is an odd number: 1
#                 Here is an odd number: 3
#                 Here is an odd number: 5
#                 Here is an odd number: 7
#                 Here is an odd number: 9
#                 Here is an odd number: 11
#                 Here is an odd number: 13
#                 Here is an odd number: 15
#                 Here is an odd number: 17
#                 Here is an odd number: 19
#                 Here is an odd number: 21
#                 Here is an odd number: 23
#                 Here is an odd number: 25
#                 Yikes! Skipping number: 27
#                 Here is an odd number: 29
#                 Here is an odd number: 31
#                 Here is an odd number: 33
#                 Here is an odd number: 35
#                 Here is an odd number: 37
#                 Here is an odd number: 39
#                 Here is an odd number: 41
#                 Here is an odd number: 43
#                 Here is an odd number: 45
#                 Here is an odd number: 47
#                 Here is an odd number: 49

# step 1: get a *valid* number from the user
# while we have something that is not valid
#   keep prompting the user for input

# number_to_skip = input('Please enter an odd number (1-50): ')
while not number_to_skip.isdigit() or int(number_to_skip) < 1 or int(number_to_skip) > 50 or int(number_to_skip) % 2 == 0:
    number_to_skip = input('Please enter an odd number (1-50): ')

# The example below *will not work* because of the order of the conditions
while int(number_to_skip) < 1 or not number_to_skip.isdigit() or int(number_to_skip) > 50 or int(number_to_skip) % 2 == 0:
    number_to_skip = input('Please enter an odd number (1-50): ')

# # keep prompting for input
# # if we have valid input, stop the loop
while True:
    number_to_skip = input('Enter an odd number (1-50): ')
    # if number_to_skip.isdigit() and 1 <= int(number_to_skip) <= 50 and int(number_to_skip) % 2 == 1:
    #     break
    if number_to_skip.isdigit() and int(number_to_skip) in range(1, 51) and int(number_to_skip) % 2 == 1:
        break

# number_to_skip = int(number_to_skip)
# step 2: do logic with the number we acquired
# for every number between 1 and 50
#   if the number is even
# skip it
#   if the number is the one that was entered
#       print the special message
#   else
#       print the number
for n in range(1, 51):
    if n % 2 == 0:
        continue
    if n == number_to_skip:
        print(f'Yikes! Skipping number {n}')
    else:
        print(f'Here is an odd number: {n}')

#     1. The `input` function can be used to prompt for input and use that input
#        in your python code. Prompt the user to enter a positive number and write
#        a loop that counts from 0 to that number. (Hints: first make sure that
#        the value the user entered is a valid number, also note that the `input`
#        function returns a string, so you'll need to convert this to a numeric
#        type.)

upper_bound = int(input('Please enter a number: '))
for n in range(0, upper_bound + 1):
    print(n)

#     1. Write a program that prompts the user for a positive integer. Next write
#        a loop that prints out the numbers from the number the user entered down
#        to 1.
starting_point = int(input('Enter the starting number'))
for n in range(starting_point, 0, -1):
    print(n)


# 1. Fizzbuzz

#     One of the most common interview questions for entry-level programmers is
#     the FizzBuzz test. Developed by Imran Ghory, the test is designed to test
#     basic looping and conditional logic skills.

#     - Write a program that prints the numbers from 1 to 100.
#     - For multiples of three print "Fizz" instead of the number
#     - For the multiples of five print "Buzz".
#     - For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1, 16):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)


# Alternate Solution
for n in range(1, 111):
    output = ''
    if n % 3 == 0:
        output += 'Fizz'
    if n % 5 == 0:
        output = f'{output}Buzz'
    if n % 7 == 0:
        output = '%sBang' % output

    # if output == '':
    #     print(n)
    # else:
    #     print(output)
    # we could rewrite the above if-else like so:
    print(n if output == '' else output)

# 1. Display a table of powers.

#     - Prompt the user to enter an integer.
#     - Display a table of squares and cubes from 1 to the value entered.
#     - Ask if the user wants to continue.
#     - Assume that the user will enter valid data.
#     - Only continue if the user agrees to.

#     Example Output

#     ```
#     What number would you like to go up to? 5

#     Here is your table!

#     number | squared | cubed
#     ------ | ------- | -----
#     1      | 1       | 1
#     2      | 4       | 8
#     3      | 9       | 27
#     4      | 16      | 64
#     5      | 25      | 125
#     ```

#     **Bonus**: Research python's format string specifiers to align the table

upper_bound = int(input('Enter a number: '))
n = 1

print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, upper_bound + 1):
    # right-aligned (default)
    print('{:6} | {:7} | {:5}'.format(n, n ** 2, n ** 3))
    # left-aligned
    # print('{:<6} | {:<7} | {:<5}'.format(n, n ** 2, n ** 3))
    # center-aligned
    # print('{:^6} | {:^7} | {:^5}'.format(n, n ** 2, n ** 3))


# 1. Convert given number grades into letter grades.

#     - Prompt the user for a numerical grade from 0 to 100.
#     - Display the corresponding letter grade.
#     - Prompt the user to continue.
#     - Assume that the user will enter valid integers for the grades.
#     - The application should only continue if the user agrees to.
#     - Grade Ranges:

#         - A : 100 - 88
#         - B : 87 - 80
#         - C : 79 - 67
#         - D : 66 - 60
#         - F : 59 - 0

#     **Bonus**

#     - Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# Alternate solution using dictionary keys and dictionary iteration:
grade_ranges = {
    'A': [100, 88],
    'B': [87, 80],
    'C': [79, 67],
    'D': [66, 60],
    'F': [59, 0],
}

grade = int(input('Enter a number grade: '))
for letter_grade in grade_ranges.keys():
    upper_bound, lower_bound = grade_ranges[letter_grade]
    if lower_bound <= grade <= upper_bound:
        print(letter_grade)


# solution from the in-class walkthrough
user_wants_to_continue = 'yes'

while user_wants_to_continue == 'yes':
    grade = int(input('Enter a number grade: '))

    if grade >= 88:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 67:
        print('C')
    elif grade >= 60:
        print('D')
    elif grade >= 0:
        print('F')

    user_wants_to_continue = input('Do you want to continue? ')

# 1. Create a list of dictionaries where each dictionary represents a book that
#    you have read. Each dictionary in the list should have the keys `title`,
#    `author`, and `genre`. Loop through the list and print out information about
#    each book.
books = [
    {
        'title': 'Data Science From Scratch',
        'author': 'Joel Grus',
        'genre': ['Data Science', 'Python', 'Programming']
    },
    {
        'title': 'Beautiful Evidence',
        'author': 'Edward Tufte',
        'genre': ['Visualizations', 'Data Science']
    },
    {
        'title': 'Oh the places you\'ll go',
        'author': 'Dr. Seuss',
        'genre': ['Whimsy', 'Childrens']
    }
]

genre_to_show = input('Enter a genre: ')

for book in books:
    if genre_to_show not in book['genre']:
        continue
    print('-------------')
    print('- title: %s' % book['title'])
    print('- author: %s' % book['author'])
    print('- genre: %s' % book['genre'])


#     1. Prompt the user to enter a genre, then loop through your books list and
#        print out the titles of all the books in that genre.

company_rates = {
    'google': 400,
    'amazon': 380,
    'facebook': 350
}

hours_worked = {
    'google': 6,
    'facebook': 10,
    'amazon': 4,
}

# for key in company_rates.keys():
#     value = company_rates[key]
#     print(f'key: {key} -- value: {value}')

total_pay = 0
for company_name in company_rates.keys():
    hourly_rate = company_rates[company_name]
    hours = hours_worked[company_name]
    company_total_pay = hourly_rate * hours
    print(f'{company_name.title()} paid me ${company_total_pay:,} this week.')
    total_pay += company_total_pay

print(f'For a total of ${total_pay:,}.')
