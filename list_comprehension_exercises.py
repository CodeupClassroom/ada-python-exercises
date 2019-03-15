# List Comprehension Exercises

# Use the code below to answer all of the exercises:

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# 1. Rewrite the above example code below using a list comprehension. Make a
#    variable named `uppercased_fruits` to hold the output of the list
#    comprehension. Output should be `['MANGO', 'KIWI', etc...]`

output = []
for fruit in fruits:
    output.append(fruit.upper())

uppercased_fruits = [fruit.upper() for fruit in fruits]

# 2. Create a variable named `capitalized_fruits` and use a list comprehension
#    to produce output like `['Mango', 'Kiwi', 'Strawberry', etc...]`

uppercased_fruits = [fruit.upper() for fruit in fruits]

# 3. Use a list comprehension to make a variable named
#    `fruits_with_more_than_two_vowels`. Hint: You'll need a way to check if
#    something is a vowel.

def count_vowels(word):
    return len([c for c in word.lower() if c in 'aeiou'])

[fruit for fruit in fruits if count_vowels(fruit) > 2]

# 4. Make a variable named `fruits_with_only_two_vowels`. The result should be
#    `['mango', 'kiwi']`
[fruit for fruit in fruits if count_vowels(fruit) == 2]

# 5. Make a list that contains each fruit with more than 5 characters
[fruit for fruit in fruits if len(fruit) > 5]

# 6. Make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit) == 5]

# 7. Make a list that contains fruits that have less than 5 characters
[fruit for fruit in fruits if len(fruit) < 5]

# 8. Make a list containing the number of characters in each fruit. Output would
#    be `[5, 4, 10, etc... ]`
[len(fruit) for fruit in fruits]

# 9. Make a variable named `fruits_with_letter_a` that contains a list of only the
#    fruits that contain the letter "a"
[fruit for fruit in fruits if 'a' in fruit]

# 10. Make a variable named `even_numbers` that holds only the even numbers
[n for n in numbers if n % 2 == 0]

# 11. Make a variable named `odd_numbers` that holds only the odd numbers
[n for n in numbers if n % 2 == 1]

# 12. Make a variable named `positive_numbers` that holds only the positive
#     numbers
[n for n in numbers if n > 0]

# 13. Make a variable named `negative_numbers` that holds only the negative
#     numbers
[n for n in numbers if n < 0]

# 14. Use a list comprehension with a conditional in order to produce a list of
#     numbers with 2 or more numerals
[n for n in numbers if len(str(n)) >= 2]
# OR
[n for n in numbers if n / 10 >= 1]

# 15. Make a variable named `numbers_squared` that contains the numbers list with
#     each element squared. Output is `[4, 9, 16, etc...]`
[n ** 2 for n in numbers]

# 16. Make a variable named `odd_negative_numbers` that contains only the numbers
#     that are both odd and negative.
[n for n in numbers if n < 0 and n % 2 == 1]

# 17. Make a variable named primes that is a list containing the prime numbers in
#     the numbers list.

import math

def is_prime(n: int) -> bool:
    '''
    returns True or False based on whether the passed number is a prime number.

    A simple way to check if a number is prime is to say that it is prime if it
    is not evenly divisible by all the whole numbers below it up to the square
    root of the number. See https://en.wikipedia.org/wiki/Trial_division

    This is a somewhat naive approach and will be very expensive for larger
    numbers.

    For more background and more sophisticated approaches, see
    https://en.wikipedia.org/wiki/Prime_number#Computational_methods
    '''
    n = abs(n) # negative numbers
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        # if it's evenly divisible, it's not a prime number
        if n % x == 0:
            return False
    # if we get past all the numbers in the loop above, then we have a prime
    # number
    return True

[n for n in numbers if is_prime(n)]
