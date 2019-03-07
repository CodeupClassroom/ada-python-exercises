# import functions_exercise as fe
# from functions_exercise import cumsum

# print(fe.calculate_tip(0.25, 20))
# print(cumsum([1, 5, 2, 3, 7]))

# # it's pretty common to see the itertools module aliased as "it"
# import itertools as it

# print(list(it.product('abc', '123')))
# print(list(it.permutations('abcde', 2)))

import json

profiles = json.load(open('./profiles.json'))

print('--- Total number of users')
print(len(profiles))

print('--- Number of active users ---')
active_users = [user for user in profiles if user['isActive']]
print(len(active_users))

print('--- Number of inactive users ---')
print(len(profiles) - len(active_users))

print('--- Grand total of balances for all users ---')
def clean_balance(bal):
    bal = bal[1:] # remove the beginning '$'
    bal = bal.replace(',', '') # remove commas
    return float(bal)

balances = [clean_balance(profile['balance']) for profile in profiles]
print(sum(balances))

print('--- Average balance per user ---')
avg = sum(balances) / len(balances)
print(round(avg, 2))

print('--- User with the lowest balance ---')
min_balance = min(balances)
user = [user for user in profiles if clean_balance(user['balance']) == min_balance][0]
print(user['name'])

print('--- User with the highest balance ---')
highest_balance_user = profiles[0]
for user in profiles[1:]:
    if clean_balance(user['balance']) > clean_balance(highest_balance_user['balance']):
        highest_balance_user = user

print(highest_balance_user['name'])

print('--- Most common favorite fruit ---')
favorite_fruits = [user['favoriteFruit'] for user in profiles]

# we'll create a dictionary where the keys are the names of the fruits, and the
# values are the number of users with that fruit as their favorite
favorite_fruit_counts = {}
for fruit in favorite_fruits:
    if fruit in favorite_fruit_counts:
        favorite_fruit_counts[fruit] += 1
    else:
        favorite_fruit_counts[fruit] = 1

# alternate fancy solution
# from collections import defaultdict
# favorite_fruit_counts = defaultdict(lambda: 0)
# for fruit in favorite_fruits:
#     favorite_fruit_counts[fruit] += 1

# Now we'll convert the dictionary to a list of key-value pairs so that we can
# sort it (dictionaries don't have an order, so they can't be sorted). We'll use
# the `sorted` function and tell it that the way we want to sort the list (using
# a lambda) is by the second item in each pair (the values, i.e. the count of
# users with that favorite fruit as their favorite). Once the list is sorted,
# the last item will be the most common favorite fruit
items = list(favorite_fruit_counts.items())
items.sort(key=lambda item: item[1])
print(items[-1][0])

print('--- Least common favorite fruit ---')
print(items[0][0])

print('--- Total number of unread messages for all users ---')
def extract_n_unread_messages(greeting: str):
    start = 'You have '
    stop = ' unread messages.'
    start_index = greeting.index(start) + len(start)
    stop_index = greeting.index(stop)
    return int(greeting[start_index:stop_index])

greetings = [user['greeting'] for user in profiles]
unread_messages = [extract_n_unread_messages(greeting) for greeting in greetings]
print(sum(unread_messages))
