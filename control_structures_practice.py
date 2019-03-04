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

weekend_days = ['saturday', 'sunday', 'sat', 'sun']
weekday = input('Enter a weekday: ')
if weekday.lower() in weekend_days:
    print('Weekend!')
else:
    print('Weekday!')

# 3. create variables and make up values for
#
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

hours_worked = 43
hourly_rate = 900
if hours_worked > 40:
    pay_at_regular_rate = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
    paycheck = pay_at_regular_rate + overtime_pay
else:
    paycheck = hourly_rate * hours_worked

print(paycheck)