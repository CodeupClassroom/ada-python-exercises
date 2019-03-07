
# f = open('control_structures_exercise.py')
# contents = f.read()
# f.close()

# # this is the preferred way:
# # this will take care of closing the file for us
# with open('control_structures_exercise.py') as f:
#     contents = f.read()

# lines = contents.split('\n')

# # print the first 10 lines of the file
# for line in lines[-10:]:
#     print(line)

# this will take care of closing the file for us
with open('control_structures_exercise.py') as f:
    # shortcut to read file as a list of lines
    lines = f.readlines()

# print the first line in the file
# print(lines[0])

# # print the first 10 lines of the file
# for line in lines[:10]:
#     print(line)

# # just print the lines that are commented out code
# for line in lines:
#     if line.startswith('#'):
#         print(line)

# as a list comprehension
# [print(line) for line in lines if line.startswith('#')]

# with open('example.txt') as f:
#     lines_1 = f.readlines()

# with open('example.txt') as f:
#     lines_2 = f.read().split('\n')

# print(lines_1)
# print('--------')
# print(lines_2)

# # don't read the file twice
# with open('example.txt') as f:
#     contents_1 = f.read()
#     contents_2 = f.read()

# print(contents_1)
# print('--------')
# print(contents_2)

# a - append
# w - truncate the file, then write to it
# x - creating a file if it doesn't exist
# with open('example2.txt', 'a') as f:
#     f.write('Good afternoon, Ada!\n')

# with open('example2.txt', 'x') as f:
#     f.write('Good afternoon, Ada!\n')

# write a program that prompts the user for a python file
# and comments out all the lines in the file
from sys import exit

filename = input('Please enter a python filename: ')
if not filename.endswith('.py'):
    print('Error: bad filename.')
    print('       {} does not end with ".py"'.format(filename))
    exit()

print('Reading file ({}) contents...'.format(filename))
with open(filename) as f:
    lines = f.read().split('\n')

# build a new list of commented out code
commented_out_code = []
for line in lines:
    if line.startswith('#') or line == '':
        commented_out_code.append(line)
    else:
        commented_out_code.append('# ' + line)

print('Writing to file: {}'.format(filename))

with open(filename, 'w') as f:
    f.write('\n'.join(commented_out_code))