print("Please enter a password to validate.")
password = input()
SpecialSym =['$', '@', '#', '%']
while True:
    if len(password) < 8:
        print("NOT MATCHED")
    elif len(password)>20:
        print("NOT MATCHED")    
    elif not any(char.isupper() for char in password):
        print("NOT MATCHED")
    elif not any(char.islower() for char in password):
        print("NOT MATCHED")
    elif not any(char.isdigit() for char in password):
        print("NOT MATCHED")
    elif not any(char in SpecialSym for char in  password):
        print("NOT MATCHED")    
    else:
        print("MATCHED")
        break
    password = input()