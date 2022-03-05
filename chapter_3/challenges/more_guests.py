# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# 	call to the end of your program informing people that you found a bigger
# 	dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


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