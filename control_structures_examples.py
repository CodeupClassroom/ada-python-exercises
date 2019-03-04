
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



pizza_preference = input('What kind of pizza do you like? ')
if pizza_preference == 'pineapple and hot sauce':
    print('Wow! What a coincidence, that is my favorite too!')
    spicy_level = int(input('How spicy would you like it? (1-5) '))
    if spicy_level == 5:
        print('Wow! That is hot!')
    elif spicy_level > 3:
        print('Can we take it down a notch?')
    else:
        print('That sounds good!')
elif pizza_preference == 'pepperoni, jalepeno, and anchovies':
    print('Hmmmm... okay')
elif pizza_preference == 'cheese':
    print('Just plain cheese... okay')
else:
    print('That is not my favorite, but lets order some!')

print('All Done')





# # only one branch will ever run
# if False:
#     print(1)
# elif True:
#     print(2)
# elif True:
#     print(3)
# else:
#     print(4)

