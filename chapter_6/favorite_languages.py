# A Dictionary of Similar Objects

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# Sarah's favorite language is C.

# Looping through all key-value pairs
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
# output:
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Ruby.
# Phil's favorite language is Python.

# This type of looping would work just as well if our dictionary stored the
# results from polling a thousand or even a million people.

# Looping Through All the Keys in a Dictionary

# The keys() method is useful when you don’t need to work with all of the
# values
# in a dictionary. Let’s loop through the favorite_languages dictionary
# and print the names of everyone who took the poll:
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in favorite_languages.keys():
	print(name.title())
# output:
# Jen
# Sarah
# Edward
# Phill

# Looping through the keys is actually the default behavior when looping
# through a dictionary, so this code would have exactly the same output if you
# wrote . . .
for name in favorite_languages:
	print(name.title())
# rather than . . .
for name in favorite_languages.keys():
	print(name.title())
# You can choose to use the keys() method explicitly if it makes your code
# easier to read, or you can omit it if you wish.

# You can access the value associated with any key you care about inside
# the loop by using the current key. Let’s print a message to a couple of friends
# about the languages they chose. We’ll loop through the names in the dictionary
# as we did previously, but when the name matches one of our friends, we’ll
# display a message about their favorite language:
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

if name in friends:
	language = favorite_languages[name].title()
	print(f"\t{name.title()}, I see you love {language}!")
# output:
# Hi Jen.
# Hi Sarah.
# 	Sarah, I see you love C!
# Hi Edward.
# Hi Phil.
#   Phil, I see you love Python!

# You can also use the keys() method to find out if a particular person
# was polled. This time, let’s find out if Erin took the poll:

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
# Erin, please take our poll!

# Looping Through a Dictionary’s Keys in a Particular Order

# Sometimes, though, you’ll want to loop through a dictionary in a 
# different order.
# One way to do this is to sort the keys as they’re returned in the for loop.
# You can use the sorted() function to get a copy of the keys in order:
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
# output:
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.

# Looping Through All Values in a Dictionary

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
# This approach pulls all the values from the dictionary without checking
# for repeats. That might work fine with a small number of values, but in a
# poll with a large number of respondents, this would result in a very repetitive
# list. To see each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique:

for language in set(favorite_languages.values()):
	print(language.title())
# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.
# we use set() to pull out the unique languages in favorite_languages.values().
# The result is a nonrepetitive list of languages that have been mentioned
# by people taking the poll

# You can build a set directly using braces and separating the elements with 
# commas:   

#           languages = {'python', 'ruby', 'python', 'c'}
# 			languages
# 			{'ruby', 'python', 'c'}

# It’s easy to mistake sets for dictionaries because they’re both wrapped in 
# braces. When you see braces but no key-value pairs, you’re probably looking 
# at a set. Unlike lists and dictionaries, sets do not retain items in any 
# specific order.

