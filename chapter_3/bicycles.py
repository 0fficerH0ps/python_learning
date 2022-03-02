bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# output ['trek', 'cannondale', 'redline', 'specialized']

# pull out the first bicycle in the list bicycles:
print(bicycles[0])
# output "trek"

print(bicycles[0].title())
# output "Trek"

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])
# output:
# cannondale
# specialized

# Python has a special syntax for accessing the last element in a list. By asking
# for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1])
# output "specialized"

# using specific values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# output "My first bicycle was a Trek"