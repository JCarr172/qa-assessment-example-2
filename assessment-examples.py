	# <QUESTION 1>

	# Given a word and a string of characters, return the word with all of the given characters
    # replaced with underscores

    # This should be case sensitive

	# <EXAMPLES>

	# one("hello world", "aeiou") → "h_ll_ w_rld"
    # one("didgeridoo", "do") → "_i_geri___"
	# one("punctation, or something?", " ,?") → "punctuation__or_something_"

def one(word, chars):
    new_word = word
    for char in range (0,len(chars)):
        new_word = new_word.replace(chars[char],'_')
    return new_word
words = one("punctation, or something?", " ,?")
print(words)

	# <QUESTION 2>

	# Given an integer - representing total seconds - return a tuple of integers (of length 4) representing 
    # days, hours, minutes, and seconds

	# <EXAMPLES>

	# two(270) → (0, 0, 4, 30)
    # two(3600) → (0, 1, 0, 0)
	# two(86400) → (1, 0, 0, 0)

	# <HINT>

    # There are 86,400 seconds in a day, and 3600 seconds in an hour

def two(total_seconds):
    days = total_seconds//86400
    hours = (total_seconds-86400*days)//3600
    minutes = (total_seconds - 86400*days - 3600*hours)//60
    seconds = total_seconds - 86400*days - 3600*hours - 60*minutes
    time = (days, hours, minutes, seconds)
    return time

print(two(345743))

	# <QUESTION 3>

	# Given a dictionary mapping keys to values, return a new dictionary mapping the values
    # to their corresponding keys

	# <EXAMPLES>

	# three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracis':'thank you'}
    # three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

    # <HINT>

    # Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
    value = list(dictionary.values())
    key = list(dictionary.keys())
    new_dict = {}
    for i in range(0,len(value)):
        print(key[i])
        d = {value[i]:key[i]}
        new_dict.update(d)
    return new_dict

print(three({'hello':'hola', 'thank you':'gracias'}))

    # <QUESTION 4>

	# Given an integer, return the largest of the numbers this integer is divisible by
    # excluding itself

    # This should also work for negative numbers

	# <EXAMPLES>

	# four(10) → 5
    # four(24) → 12
    # four(7) → 1
    # four(-10) → 5

def four(number):
    divisors = []
    for num in range(1,number):
        if number%num == 0:
            divisors.append(num)
    divisors.sort()
    return divisors[-1]
print(four(24))

    # <QUESTION 5>

	# Given an string of characters, return the character with the lowest ASCII value

	# <EXAMPLES>

	# five('abcdef') → 'a'
    # four('LoremIpsum') → 'I'
    # four('hello world!') → ' '

def five(chars):
    char = sorted(chars)
    return char[0]

print(five('hello world!'))
