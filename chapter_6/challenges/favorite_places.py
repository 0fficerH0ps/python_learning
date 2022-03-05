# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = { 'jack': {'new england', 'denmark', 'scotland'},
					'sam': {'his kitchen', 'his bed'},
					'sarah': {'her roof', 'the local arcade'},
					'ruby': {'her house'}
					}

for name, place in favorite_places:
	if len(favorite_places[place]) == 1:
		print(f"{name.title()}'s favorite place to be is:\n{place.title()}")
	else:
		print(f"{name.title()}'s favorite plcaes to be are:\n{place.title()}")