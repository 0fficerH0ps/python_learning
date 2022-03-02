# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.


people = {  'person_1': { 
				'first': 'jack', 
				'last': 'smith', 
				'age': '41',
				'city': 'greenville',
				}, 
			'person_2': {
				'first': 'billy', 
				'last': 'bobbert', 
				'age': '87',
				'city': 'tucket',
				},
			'person_3': {
				'first': 'sarah',
				'last': 'johntson',
				'age': '54',
				'city': 'johnsvill',
				},

}

for person, person_info in people.items():
	print(f"\n{person.title()}")
	full_name = f"{person_info['first']} {person_info['last']}"
	age = f"{person_info['age']}"
	city = f"{person_info['city']}"

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tCity: {city.title()}")


