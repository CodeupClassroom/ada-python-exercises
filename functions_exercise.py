# https://ds.codeup.com/4.4_functions/

def is_two(something):
    if something == 2 or something == '2':
        return True
    else:
        return False

def is_two(something):
    return something == 2 or something == '2'

print('is_two(2) = %s' % is_two(2))
print('is_two("2") = %s' % is_two('2'))
print('is_two(3) = %s' % is_two(3))
print('is_two([]) = %s' % is_two([]))
print('is_two(None) = %s' % is_two(None))

VOWELS = 'aeiou'

def is_vowel(a_string):
    return a_string in VOWELS

print("is_vowel('a') == %s" % is_vowel('a'))
print("is_vowel('e') == %s" % is_vowel('e'))
print("is_vowel('y') == %s" % is_vowel('y'))
print("is_vowel('b') == %s" % is_vowel('b'))

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(a_string):
    # debuggin print statements might look like this:
    # print('is_consonant was called!')
    # print('a_string is %s' % a_string)
    return_value = not is_vowel(a_string)
    # print('return_value is %s' % return_value)
    return return_value

# code to test my functions
print("is_consonant('a') == %s" % is_consonant('a'))
print("is_consonant('e') == %s" % is_consonant('e'))
print("is_consonant('y') == %s" % is_consonant('y'))
print("is_consonant('b') == %s" % is_consonant('b'))

def cap_if_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        # return word.capitalize()
        return word[0].upper() + word[1:].lower()
    else:
        return word

# # clever solution
# def cap_if_consonant(word):
#     first_letter, *rest_of_letters = word
#     return first_letter.upper() + rest_of_letters.lower() if is_consonant(first_letter) else word

print("cap_if_consonant('codeup') == %s" % cap_if_consonant('codeup'))
print("cap_if_consonant('ada') == %s" % cap_if_consonant('ada'))
print("cap_if_consonant('Codeup') == %s" % cap_if_consonant('Codeup'))
print("cap_if_consonant('Ada') == %s" % cap_if_consonant('Ada'))

def calculate_tip(percentage, total):
    return percentage * total

print("calculate_tip(0.2, 20) == %s" % calculate_tip(0.2, 20))
print("calculate_tip(0.15, 10) == %s" % calculate_tip(0.15, 10))

# if we wanted the total bill including the tip...
def calculate_tip(percentage, total):
    amount_to_tip = percentage * total
    return total + amount_to_tip

def apply_discount(price, discount_percent):
    discount_amount = price * discount_percent
    return price - discount_amount

# another way to write it
# def apply_discount(price, discount_percent):
#     return price * (1 - discount_percent)

print("apply_discount(10, 0.2) == %s" % apply_discount(10, 0.2))
print("apply_discount(50, 0.8) == %s" % apply_discount(50, 0.8))

def handle_commas(a_string):
    string_without_commas = a_string.replace(',', '')
    return int(string_without_commas)

print("handle_commas('1,234') == %s" % handle_commas('1,234'))
print("handle_commas('1,234,567') == %s" % handle_commas('1,234,567'))

def get_letter_grade(numerical_grade):
    if numerical_grade >= 88:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 67:
        return 'C'
    elif numerical_grade >= 60:
        return 'D'
    elif numerical_grade >= 0:
        return 'F'

print("get_letter_grade(92) == %s" % get_letter_grade(92))
print("get_letter_grade(84) == %s" % get_letter_grade(84))
print("get_letter_grade(12) == %s" % get_letter_grade(12))

def remove_vowels(a_string):
    return (a_string.replace('a', '')
        .replace('e', '')
        .replace('i', '')
        .replace('o', '')
        .replace('u', ''))

def remove_vowels(word):
    print('remove_vowels was called!')
    word_list = []
    for v in word:
        print('Start of our for loop, word_list == %s' % word_list)
        print(f'looking at letter: {v}')
        if is_vowel(v):
            print('skipping letter! it is a vowel')
            continue
        word_list.append(v)
    print('about to exit remove_vowels, word_list == %s' % word_list)
    return ''.join(word_list)

# def remove_vowels(a_string):
#     return ''.join([letter for letter in a_string if not is_vowel(letter)])

def remove_vowels(a_string):
    for vowel in 'aeiou':
        a_string = a_string.replace(vowel, '')
    return a_string

remove_vowels('abcdef')

LETTERS = ' _abcdefghijklmnopqrstuvwxyz0123456789'

def normalize_name(a_string):
    a_string = a_string.lower()
    valid_characters = []
    for character in a_string:
        if character in LETTERS:
            valid_characters.append(character)
    return ''.join(valid_characters).strip().replace(' ', '_')

print("normalize_name('Name') == {}".format(normalize_name('Name')))
print("normalize_name('First Name') == {}".format(normalize_name('First Name')))
print("normalize_name('% Completed') == {}".format(normalize_name('% Completed')))


def cumsum(numbers):
    sums = [numbers[0]]
    for current_number in numbers[1:]:
        last_number = sums[-1]
        next_number = last_number + current_number
        sums.append(next_number)
    return sums

def cumsum(num_list):
    return [sum(num_list[: i + 1]) for i in range(len(num_list))]

print("cumsum([1, 1, 1]) == %s" % cumsum([1, 1, 1]))
print("cumsum([1, 2, 3]) == %s" % cumsum([1, 2, 3]))
print("cumsum([1, 2, 3, 4]) == %s" % cumsum([1, 2, 3, 4]))
print("cumsum([1, -2, 1]) == %s" % cumsum([1, -2, 1]))

print('\n' * 10)

