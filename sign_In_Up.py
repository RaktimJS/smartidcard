import os, hashlib, json, datetime

os.system("cls")




def uid():
        """
        Generates a unique 12-digit ID based on current UTC timestamp
        Returns format: "XXXX-XXXX-XXXX"
        """

        t = datetime.datetime.now(datetime.timezone.utc)
        micros_since_epoch = int(t.timestamp() * 1_000_000)
        s = f"{micros_since_epoch:012d}"[-12:]  # keep the last 12 digits

        return f"{s[0:4]}-{s[4:8]}-{s[8:12]}"

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
