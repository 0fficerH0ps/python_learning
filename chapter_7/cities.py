prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# You can use the break statement in any of Python’s loops. For example, you could use
# break to quit a for loop that’s working through a list or a dictionary.
