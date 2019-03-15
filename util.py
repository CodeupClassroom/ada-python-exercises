SIDES_ON_A_DICE = 6

import env
from sqlalchemy import create_engine

def sayhowdy():
    '''
    A more regionally-efficient version of sayhello

    use this mostly in Texas, not so much elsewhere

    >>> sayhowdy()
    "Howdy, Y'all"

    Does not accept any arguments
    '''
    return 'Howdy, Y\'all!'

def sayhello():
    'Returns a nice message to the caller.'
    return 'Hello, World!'

def get_url_string(user, password, host, db, driver='pymysql'):
    return f'mysql+{driver}://{user}:{password}@{host}/{db}'

def get_connection(db):
    url = get_url_string(user=env.user, password=env.password, host=env.host, db=db)
    return create_engine(url)

if __name__ == '__main__':
    print('Hello, Ada! Are you excited for early release?')
