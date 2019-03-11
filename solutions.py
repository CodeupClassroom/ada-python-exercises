def isnegative(n):
    return n < 0

# loop through the numbers and increment a counter variable
# for every even number
def count_evens(numbers):
    n_evens = 0
    for n in numbers:
        if n % 2 == 0:
            n_evens += 1
    return n_evens

def count_evens(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return len(even_numbers)

def increment_odds(numbers):
    incremented_numbers = []
    for n in numbers:
        if n % 2 == 1:
            incremented_numbers.append(n + 1)
        else:
            incremented_numbers.append(n)
    return incremented_numbers

def increment_odds(xs):
    return [x + 1 if x % 2 == 1 else x for x in xs]

def average(numbers):
    sum = 0
    for n in numbers:
        sum += n
    length = len(numbers) 
    return sum / length

def average(numbers):
    return sum(numbers) / len(numbers)

def name_to_dict(name: str) -> dict:
    parts = name.split(' ')
    d = {}
    d['first_name'] = parts[0]
    d['last_name'] = parts[1]
    return d

def name_to_dict(name: str) -> dict:
    first_name, last_name = name.split(' ')
    return {'first_name': first_name, 'last_name': last_name}

def capitalize_names(people: list) -> list:
    capitalized = []
    for person in people:
        print(person)
        capitalized.append({
            'first_name': person['first_name'].title(),
            'last_name': person['last_name'].title(),
        })
    return capitalized

def capitalize_names(people: list) -> list:
    capitalized_names = []
    for person in people:
        capitalized_person = {}
        capitalized_person['first_name'] = person['first_name'].title()
        capitalized_person['last_name'] = person['last_name'].title()
        capitalized_names.append(capitalized_person)
    return capitalized_names

def capitalize_names(people: list) -> list:
    capitalized_names = []
    for person in people:
        d = {}
        for k in person.keys():
            d[k] = person[k].title()
            capitalized_names.append(d)
    return capitalized_names

def count_vowels(word: str) -> int:
    n_vowels = 0
    for letter in word:
        if letter in 'aeiou':
            n_vowels += 1
    return n_vowels

def count_vowels(word: str) -> int:
    vowels = [letter for letter in word if letter in 'aeiou']
    return len(vowels)

def analyze_word(word: str) -> dict:
    return dict(word=word, n_letters=len(word), n_vowels=count_vowels(word))