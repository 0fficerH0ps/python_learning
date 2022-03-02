# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the 
# information you have stored about it.

cities = {
			'city 1': {
				'country': 'a place',
				'population': '2',
				'fact': 'The bugs are edable',
			},
			'city 2': {
				'country': 'another place',
				'population': '5681.2518965',
				'fact': 'More information means more knowledge',
			},
			'city 3': {
				'country': 'somewhere over a rainbow',
				'population': 'leper-cans',
				'fact': 'Only fun stuff happens here',
			},
}

for city_name, city_info in cities.items():
	print(f"\nCity name is: {city_name.title()}")
	print(f"This city is located in: {city_info['country'].title()}.")
	print(f"This city has a population of: {city_info['population']}.")
	print(f"A cool fact about this city is: {city_info['fact']}.")