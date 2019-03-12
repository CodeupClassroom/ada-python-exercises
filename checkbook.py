'''
Python Script for managing a text file checkbook.

We'll store the data that makes up the check book in a text file whose locations
is specified by the DATA_FILE constant.

Transactions are stored as numbers on separate lines of the file. Debits are
negative numbers, credits are positive.

Here is an example of what the data file will look like:

    100
    -10
    -20

Which gives a balance of $70
'''

from sys import exit
from os import path

DEBUG = False

def debug(msg):
    '''
    A function solely for debugging.

    Will show messages if the global DEBUG flag is set, otherwise will hide
    them.
    '''
    if DEBUG:
        print(msg)

DATA_FILE = 'transactions.txt'

MENU = '''
1) View Balance
2) Make a Withdrawal
3) Make a Deposit
4) View Transactions
5) Exit
'''

def get_transactions():
    with open(DATA_FILE) as f:
        lines = f.read().strip().split('\n')
    transactions = [float(line) for line in lines if line != '']
    return transactions

def ensure_data_file_exists():
    if not path.exists(DATA_FILE):
        print('ERROR: {} not found!'.format(DATA_FILE))
        exit(1)

def view_balance():
    transactions = get_transactions()
    current_balance = sum(transactions)
    print('Your balance is {:,}'.format(current_balance))

def make_withdrawal():
    amount = input('How much are you withdrawing? ')
    amount = float(amount) # TODO: validate input
    with open(DATA_FILE, 'a') as f:
        f.write(f'\n-{amount}')
    print('Added a debit of ${:,}'.format(amount))

def make_deposit():
    amount = input('How much are you depositing? ')
    amount = float(amount) # TODO: validate input
    with open(DATA_FILE, 'a') as f:
        f.write(f'\n{amount}')
    print('Added a credit of ${:,}'.format(amount))


def view_transactions():
    transactions = get_transactions()
    print('TYPE   | AMOUNT')
    print('-------|-------')
    for amount in transactions:
        transaction_type = 'DEBIT' if amount < 0 else 'CREDIT'
        print('{:6} | {:,}'.format(transaction_type, abs(amount)))

def goodbye():
    print('Have a great day!')
    exit()

MENU_OPTIONS = {
    1: view_balance,
    2: make_withdrawal,
    3: make_deposit,
    4: view_transactions,
    5: goodbye,
}


def get_menu_choice():
    debug('[get_menu_choice] called')
    print(MENU)
    choice = input('Your selection: ')
    debug('[get_menu_choice] choice = %s' % choice)
    if choice.isdigit() and int(choice) in MENU_OPTIONS.keys():
        debug('[get_menu_choice] choice is good, returning')
        return int(choice)
    else:
        debug('[get_menu_choice] bad choice, recursing')
        return get_menu_choice()

def main():
    ensure_data_file_exists()
    debug('[main] called!')
    choice = get_menu_choice()
    debug('[main] choice = %s' % choice)
    fn = MENU_OPTIONS[choice]
    debug('[main] fn = {}'.format(fn))
    fn()
    main()

if __name__ == '__main__':
    main()
