
# i_like_coffee = True
# im_in_the_mood_to_chat = False

# if i_like_coffee and im_in_the_mood_to_chat:
#     print('I like coffee!')
#     print(aljhsdbfjhabsdjfhb) # NameError
#     # !$%&!@#$*(!@#&$(@!&#*$&!@*#$)) # SyntaxError
#     print('Coffee is the best!')
# else:
#     print('Well okay, maybe we can have some tea')


# print('1')
# print(+-=-**@!) # SyntaxError
# print('2')
# print('3')



# pizza_preference = input('What kind of pizza do you like? ')
# if pizza_preference == 'pineapple and hot sauce':
#     print('Wow! What a coincidence, that is my favorite too!')
#     spicy_level = int(input('How spicy would you like it? (1-5) '))
#     if spicy_level == 5:
#         print('Wow! That is hot!')
#     elif spicy_level > 3:
#         print('Can we take it down a notch?')
#     else:
#         print('That sounds good!')
# elif pizza_preference == 'pepperoni, jalepeno, and anchovies':
#     print('Hmmmm... okay')
# elif pizza_preference == 'cheese':
#     print('Just plain cheese... okay')
# else:
#     print('That is not my favorite, but lets order some!')

# print('All Done')





# # only one branch will ever run
# if False:
#     print(1)
# elif True:
#     print(2)
# elif True:
#     print(3)
# else:
#     print(4)





# ---------------- Loops --------------

# for n in range(1, 11):
#     print(n)


# dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},
#            {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},
#            {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},
#            {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},
#            {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]

# print('Here is a summary of our data:')
# for feature in dataset:
#     if feature['type'] == 'boolean':
#         print(feature['name'])
#         for x in feature['data']:
#             print(f'    - {x}')


# i = 5
# while 10 >= i:
#     print(i)
#     i += 1

# while True:
#     print('Will you see this?')

# user_input = input('Please enter a number: ')
# # until the user enters something that looks like a number,
# # keep prompting for input
# while not user_input.isdigit():
#     user_input = input('HeY!!!! Give me a number: ')

# user_input = int(user_input)
# print('Your number plus 100 is %d' % (user_input + 100))


# for i in range(100):
#     print(i)
#     if i >= 10:
#         break

for i in range(1, 8):
    # skip the numbers evenly divisible by 3
    is_divisible_by_three = i % 3 == 0
    if is_divisible_by_three:
        continue
    print(i)

