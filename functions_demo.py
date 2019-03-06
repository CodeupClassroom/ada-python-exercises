# get an odd number from the user in the range (1-50)

def is_even(n):
    return n % 2 == 0

# get a integer from the user
def get_integer_input(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        print('Error: {} is not an integer'.format(user_input))
        return get_integer_input(prompt)
    return int(user_input)

# will read user input from the terminal
def get_odd_number_input(prompt):
    user_input = get_integer_input(prompt)
    if is_even(user_input):
        print('Error: {} is an even number'.format(user_input))
        return get_odd_number_input(prompt)
    return user_input

# get an odd number in a range
def get_odd_number_in_range(prompt, min, max):
    user_input = get_odd_number_input(prompt)
    if user_input < min or user_input > max:
        msg = 'Error: {} is not in the range ({}-{})'
        print(msg.format(user_input, min, max))
        return get_odd_number_in_range(prompt, min, max)
    return user_input

print('<<< Program Start! >>>')

prompt = 'Please enter an odd integer (1-100): '
inputted_number = get_odd_number_in_range(prompt, 1, 100)

print('user gave us: {}'.format(inputted_number))
print('user gave us a {}'.format(type(inputted_number)))

get_odd_number_in_range('enter a number: ', 1, 50)

