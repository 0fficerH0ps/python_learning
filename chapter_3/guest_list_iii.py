# Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

guests = ['albert einstein', 'jason mamoa', 'jared stevenson', 'greatgrandpa']
message = f"{guests[0].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)

message = f"{guests[1].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)

message = f"{guests[2].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)

message = f"{guests[3].title()}, please join me and a few other friends for dinner tonight, my treat!"
print(message)

number = len(guests)
message = f"Hello all, {number} individuals have been invited to dinner tonight."
print(message)
