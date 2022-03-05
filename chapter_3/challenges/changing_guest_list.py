# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# 	of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# 	the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# 	in your list.

guests = ['albert einstein', 'jason mamoa', 'jared stevenson', 'greatgrandpa']
message = f"{guests[0].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[1].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[2].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)
message = f"{guests[3].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)

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
