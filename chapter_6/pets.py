# 6-8. Pets: Make several dictionaries, where each dictionary represents a 
# different pet. In each dictionary, include the kind of animal and the owner’s
# name.
# Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do, print everything you know about each pet.

# for key in x:
# 	print(key, x[key])
# for k, v in x.items():
# 	print(k, v)

# pet dictionaries
# pet_# = {'pet name': 'name', 'type': 'type_name', 'owner': 'owner_name',}
pets = [
	{
		'pet_1': {
			'pet_name':'jasper', 
			'type': 'grifton', 
			'owner': 'mike',
		}
	},
	{
		'pet_2': {
			'pet_name': 'pudge', 
			'type': 'dog', 
			'owner': 'tom',
		}
	},
	{
		'pet_3': {
			'pet_name': 'hexy', 
			'type': 'cat', 
			'owner': 'sarah',
		}
	},
]

for pet in pets:
	print(pet)
