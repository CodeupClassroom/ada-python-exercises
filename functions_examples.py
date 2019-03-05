# # Built-in functions

# int
# int('3')

# print
# print()

# user-defined functions

# def some_function_name(function_parameter1, function_parameter2):
#     # body of the function
#     return


# function control flow
# def sayhello():
#     print(2)
#     print('Hello, World!')


# print(1)
# sayhello()
# print(3)

# def sayhello(name):
#     print('Hello, %s!' % name)


# sayhello('World')
# sayhello('Ada')
# sayhello()

# parameters: placeholders that are part of the function def
# arguments: values the function is called with

# # return values
# def sayhello(name):
#     return 'Hello, %s!' % name


# # we've worked with return values in the past
# # userinput = int(input('please enter a number'))

# return_value = sayhello('Ada')

# print(return_value)


# x = 2
# y = 3

# result = x + y
# # result = 2 + 3
# # result = 5

# print(result)


# # prefer functions that return
# def double(n):
#     return n * 2


# result = double(3)
# # result = 6
# print(result)

# print(double(double(3)))
# # print(double(double(3)))
# # print(double(6))
# # print(12)

# def sayhello(name='World', greeting='Hello'):
#     return '%s, %s!' % (greeting, name)


# # calling a function with positional arguments
# print(sayhello('Ada', 'Salutations'))
# print(sayhello('Salutations', 'Ada'))
# print(sayhello('Ada'))
# print(sayhello())
# # calling a function with keyword arguments
# print(sayhello(name='Ada', greeting='Hey there'))
# print(sayhello(greeting='Hey there', name='Ada'))
# print(sayhello())

# positional arguments: order is important
# keyword arguments: the name is important
# keyword argument must come after positional arguments

# def sayhello(name, greeting='Hello', n_times=1):
#     # name = 'Ada', greeting = 4, n_times = 1
#     for _ in range(n_times):
#         print('%s, %s!' % (greeting, name))


# sayhello(n_times=16, name='Ada', greeting='Hello')

# define a sayhello function that accepts a name,
# greeting, and punctuation
#
# practice calling the function with both
# positional and keyword arguments
#
# bonus: how many different errors can you produce
# by calling the function in different ways
# def sayhello(name, greeting, punctuation):
#     print(f'{greeting}, {name}{punctuation}')


# # NoneType
# return_value = sayhello('Ada', 'What\'s up', '!!!')
# print(return_value)

# def my_function(x, y):
#     print('<< inside of my_function >>')
#     print(f'   x: {x}')
#     print(f'   y: {y}')
#     if x > y:
#         return 'A'
#     elif y > x:
#         return 'B'
#     else:
#         return 'C'


# x = 13
# y = 2

# print(my_function(1, 1))
# print('<< outside of my_function >>')
# print(f'   x: {x}')
# print(f'   y: {y}')

# def sayhello(name, greeting):
#     return '{}, {}!'.format(greeting, name)


# name = 'Ada'
# greeting = 'Greetings'

# arguments = ['Ada', 'Greetings']

# print(sayhello(*arguments))

# def sayhello(*names, greeting='Hello'):
#     print(type(names))
#     print(names)
#     for name in names:
#         print('{}, {}!'.format(greeting, name))


# # names = ['Ada', 'Codeup', 'Maggie', 'Zach']
# # sayhello(*names)

# sayhello('Ada', 'Codeup', 'Maggie', 'Zach', greeting='Hey')

# def kwargs_example(**kwargs):
#     print(type(kwargs))
#     print(kwargs)


# kwargs_example(
#     name='Ada',
#     size=18,
#     alpha=0.05,
#     x=96
# )


# def makedict(**kwargs):
#     d = {}
#     for k in kwargs.keys():
#         value = kwargs[k]
#         d[k] = value
#     return d

# def sayhello(greeting='Hello', name='World'):
#     return f'{greeting}, {name}!'


# kwargs = {'name': 'Ada', 'greeting': 'Hey'}

# print(sayhello(**kwargs))

increment = lambda x: x + 1

print(increment(6))

print('------')

print((lambda x: x - 1)(7))