from validators import email


print("---------------------- Welcome to the real world Login application -------------------------")
user_input = input("Enter Login for Login\nEnter Sign up For registration\nForget password to reset password\n").lower()

user = {}

def signUp(user_name, user_emial, user_password):
    
    user['User'] = user_name
    user['Email'] = user_emial
    user['Password'] = user_password

    print("You have successfully registered: ")
    return user

def login(user_name, user_email):
    if user_name and user_email in user:
        print("Welcome")
    else:
        print("incorrect user or password")



name = input("Select a user name for your account: ")
emeil = input("Enter a valid email address to be registered: ")
passwor = input("Enter a valid password with atleast 8 characters: ")





if user_input == 'Signup':
    print(signUp(name, emeil, passwor))

elif user_input == 'login':
    login(emeil, passwor)
    


# print("you have successfully registered")



