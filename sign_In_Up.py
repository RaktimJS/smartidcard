import os, hashlib

os.system("cls")

print()
print("Enter 1 to sign up as an institute")
print("Enter 2 to sign up as a student")
print("Enter 3 to sign in\n")




def studentSignUp():
        pass

def instituteSignUp():
        pass

def signIn():
        pass




while True:
        selector = input("Enter your choice from the above list (EXCEEDING VALUES WILL BE CLIPPED TO NEAREST LIMIT): ")

        try:
                selector = int(selector)

                if selector < 1:
                        selector = 1
                elif selector > 3:
                        selector = 3

                break
        except ValueError or EOFError:
                print("Invalid Input\n")

if selector == 1:
        print("\nSIGN UP AS AN INSTITUTE")
        print    ("-----------------------\n")
elif selector == 2:
        print("\nSIGN UP AS A STUDENT")
        print    ("--------------------\n")
else:
        print("\nSIGN IN")
        print    ("-------\n")
