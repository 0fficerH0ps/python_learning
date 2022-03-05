# Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

# chap 3.3 functions
months = ['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']
print(months)

print(sorted(months))
print(months)

months.sort(reverse=True)
print(months)

months.reverse()
print(months)
months.reverse()
print(months)

months.sort()
print(months)
months.sort(reverse=True)
print(months)

number = len(months)
print(number)

# chap 3.2 functions
message = f"Hello all. It would seem {months[0].title()} no longer wants to be a month."
print(message)

months[0] = 'gorskin'
print(months)

months.insert(4,'lakeena')
print(months)

name = months.pop(1)
message = f"I'm sorry {name.title()}, you you are no longer a month."
print(message)
print(months)

months.append('witcher')
print(months)

del months[7]
del months[9]
print(months)


# chapter 3.1 functions
print(months[6])
print(months[2])

message = f"Hello {months[9].title()} thank you for being such a good month."
print(message)
message = f"Hello {months[5].title()} thank you for being such a good month."
print(message)
