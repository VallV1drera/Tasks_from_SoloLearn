contacts = [ 
    ('James', 42), 
    ('Amy', 24), 
    ('John', 31), 
    ('Amanda', 63), 
    ('Bob', 18) 
]

name = input()
found = False

for contact in contacts:
    if contact[0] == name:
        print(f"{contact[0]} is {contact[1]}")
        found = True
        break

if not found:
    print("Not Found")