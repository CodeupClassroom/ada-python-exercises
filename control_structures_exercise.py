# 1. Conditional Basics
# 1. prompt the user for a day of the week, print out whether the day is Monday
#    or not

# weekday = input('Please enter a weekday: ')
# print(f'weekday = {weekday}')
# if weekday == 'Monday':
#     print("Sounds like someone has a case of the Mondays!")
# else:
#     print('It is not Monday')

# 2. prompt the user for a day of the week, print out whether the day is a
#    weekday or a weekend

# weekday = input('Please enter a day of the week: ')
# if weekday == 'Saturday' or weekday == 'Sunday':
#     print('It is a weekend')
# else:
#     print('It is a weekday')

# weekday = input('Please enter a day of the week: ')
# if weekday.lower().startswith('s'):
#     print('It is a weekend')
# else:
#     print('It is a weekday')

# weekend_days = ['saturday', 'sunday', 'sat', 'sun']
# weekday = input('Enter a weekday: ')
# if weekday.lower() in weekend_days:
#     print('Weekend!')
# else:
#     print('Weekday!')

# hours_worked = 43
# hourly_rate = 900
# if hours_worked > 40:
#     pay_at_regular_rate = 40 * hourly_rate
#     overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
#     paycheck = pay_at_regular_rate + overtime_pay
# else:
#     paycheck = hourly_rate * hours_worked

# print(paycheck)

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

# i = 5
# while i <= 15:
#     print(i)
#     i += 1

#         - Create a while loop that will count by 2's starting with 0 and ending
#           at 100. Follow each number with a new line.

# i = 0
# while i <= 100:
#     print(i)
#     i += 2

#         - Alter your loop to count backwards by 5's from 100 to -10.
# i = 100
# while i >= -10:
#     print(i)
#     i -= 5

# i = 2
# while True:
#     print(len(str(i)))
#     i = i ** 2

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

# i = 2
# while i < 1_000_000:
#     print(i)
#     i *= i
#     # same as
#     # i = i ** 2

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

# i = 100
# while i >= 5:
#     print(i)
#     i -= 5

# for n in range(100, 0, -5):
#     print(n)

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

# x = int(input('Please enter a number: '))

# for n in range(1, 11):
#     output = '{} x {} = {}'.format(x, n, x * n)
#     print(output)


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

# for n in range(1, 10):
#     print(str(n) * n)


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

#     1. The `input` function can be used to prompt for input and use that input
#        in your python code. Prompt the user to enter a positive number and write
#        a loop that counts from 0 to that number. (Hints: first make sure that
#        the value the user entered is a valid number, also note that the `input`
#        function returns a string, so you'll need to convert this to a numeric
#        type.)

#     1. Write a program that prompts the user for a positive integer. Next write
#        a loop that prints out the numbers from the number the user entered down
#        to 1.

# 1. Fizzbuzz

#     One of the most common interview questions for entry-level programmers is
#     the FizzBuzz test. Developed by Imran Ghory, the test is designed to test
#     basic looping and conditional logic skills.

#     - Write a program that prints the numbers from 1 to 100.
#     - For multiples of three print "Fizz" instead of the number
#     - For the multiples of five print "Buzz".
#     - For numbers which are multiples of both three and five print "FizzBuzz".

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

# 1. Create a list of dictionaries where each dictionary represents a book that
#    you have read. Each dictionary in the list should have the keys `title`,
#    `author`, and `genre`. Loop through the list and print out information about
#    each book.

#     1. Prompt the user to enter a genre, then loop through your books list and
#        print out the titles of all the books in that genre.
