# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# 	message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# 	names remain in your list. Each time you pop a name from your list, print
# 	a message to that person letting them know you’re sorry you can’t invite
# 	them to dinner.
# • Print a message to each of the two people still on your list, letting them
# 	know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# 	list. Print your list to make sure you actually have an empty list at the end
# 	of your program.

# part 1
guests = ['albert einstein', 'jason mamoa', 'jared stevenson', 'greatgrandpa']
message = f"{guests[0].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[1].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[2].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[3].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)


# part 2
message = f"Hello all. It would seem {guests[0].title()} cannot make it to dinner tonight. He sends his apologies."
print(message)

guests[0] = 'sarah salts'
print(guests)

message = f"{guests[0].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[1].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[2].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[3].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)


# part 3
message = "Hello all. I have aquired a larger table for tonights dinner. I will be inviting a few more guests. New invitations to be sent shortly."
print(message)

guests.insert(0,'adamn sandler')
guests.insert(4,'jackie chan')
guests.append('witcher')
print(guests)

message = f"{guests[0].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[1].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[2].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[3].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[4].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[5].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[6].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)


# part 4
message = "Hello all. Saddly I have been informed that my new table will not arrive on time for dinner. I will only be able to have two of you over for dinner tonight. Let the games begin."
# I used randomly generated numbers to select which guests would be kicked off the guest list.
name = guests.pop(1)
message = f"I'm sorry {name.title()}, you will not be joining us for dinner tonight."
print(message)
print(guests)

name = guests.pop(0)
message = f"I'm sorry {name.title()}, you will not be joining us for dinner tonight."
print(message)
print(guests)

name = guests.pop(2)
message = f"I'm sorry {name.title()}, you will not be joining us for dinner tonight."
print(message)
print(guests)

name = guests.pop(0)
message = f"I'm sorry {name.title()}, you will not be joining us for dinner tonight."
print(message)
print(guests)

name = guests.pop(2)
message = f"I'm sorry {name.title()}, you will not be joining us for dinner tonight."
print(message)
print(guests)

message = f"Hello all, {guests[0]} and {guests[1]} are invited to join me for dinner tonight."
print(message)

del guests[1]
del guests[0]
print(guests)