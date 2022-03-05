# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

pets = [
	{'pet_name':'jasper', 
	'type': 'grifton', 
	'owner': 'mike',},
	
	{'pet_name': 'pudge', 
	'type': 'dog', 
	'owner': 'tom',},
	
	{'pet_name': 'hexy', 
	'type': 'cat', 
	'owner': 'sarah',},
	
]

print(pets[0])
# {'pet_name': 'jasper', 'type': 'grifton', 'owner': 'mike'}
print(pets[1])
# {'pet_name': 'pudge', 'type': 'dog', 'owner': 'tom'}
print(pets[2])
# {'pet_name': 'hexy', 'type': 'cat', 'owner': 'sarah'}

print(pets)
# [{'pet_name': 'jasper', 'type': 'grifton', 'owner': 'mike'}, 
# {'pet_name': 'pudge', 'type': 'dog', 'owner': 'tom'}, 
# {'pet_name': 'hexy', 'type': 'cat', 'owner': 'sarah'}]

print(pets[0]['pet_name']) # jasper
print(pets[0]['type']) # grifton
print(pets[0]['owner']) # mike

print(pets[1]['pet_name']) # pudge
print(pets[1]['type']) # dog
print(pets[1]['owner']) # tom

print(pets[2]['pet_name']) # hexy
print(pets[2]['type']) # cat
print(pets[2]['owner']) # sarah

