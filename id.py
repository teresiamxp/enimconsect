user = ('Mark', 'Watney')

def login():
    user = ('Melissa', 'Lewis')  # Shadows the name 'user' from the outer scope
    print(user)

login()  # Output: ('Melissa', 'Lewis')
print(user)  # Output: ('Mark', 'Watney')
