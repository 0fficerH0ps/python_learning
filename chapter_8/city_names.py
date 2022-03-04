# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
    """Return formatted city and country."""
    place = f"{city}, {country}"
    return place.title()

while True:
    print("\nEnter a city and country: ")
    print("(enter 'q' at any time to quit)")

    city_name = input("City name: ")
    if city_name == 'q':
        break
    
    country_name = input("Country name: ")
    if country_name == 'q':
        break

    formatted_place = city_country(city_name, country_name)
    print(formatted_place)

# city_country('frederiksberg', 'denmark')
# city_country('billund', 'denmark')
# city_country('sorø', 'denmark')
# Tested, all work.