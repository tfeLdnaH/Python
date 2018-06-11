from operator import itemgetter

users = [
    {'fname': 'Anderson', 'lname': 'Morita'},
    {'fname': 'Tati', 'lname': 'Asato'},
    {'fname': 'Tom', 'lname': 'Hanks'},
    {'fname': 'Tom', 'lname': 'Robert'},
    {'fname': 'Tom', 'lname': 'Jones'},
    {'fname': 'Mik', 'lname': 'Tyson'},
    {'fname': 'Jhon', 'lname': 'Kenedy'},
    ]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print("----")
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)

