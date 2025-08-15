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


def signUp():
        id = uid()
        print("Your school ID is:", id)

        # Email -------------------
        email = input("\nEnter your email: ")

        # Name --------------------
        name = input("Enter the name of the school: ")

        # Password ----------------
        print("\nPassword must 1) be at least 8 characters long")
        print("\t      2) have alteast 1 upper case letter")
        print(f"\t      3) have alteast 1 special symbol (_, !, @, #, $, %, &)")
        print("\t      4) have alteast 1 digit")

        hasUpper = False
        hasSpecialSymbol = False
        hasDigit = False

        while True:
                pswrd = input(f"\nEnter a password: ")

                i = 0

                if len(pswrd) >= 8:
                        for i in pswrd:
                                if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and hasUpper == False:
                                        hasUpper = True
                                        i = 0

                        for i in pswrd:
                                if i in "_!@#$%&" and hasSpecialSymbol == False:
                                        hasSpecialSymbol = True
                                        i = 0

                        for i in pswrd:
                                if i in "1234567890" and hasDigit == False:
                                        hasDigit = True
                                        i = 0

                        if hasUpper == True and hasSpecialSymbol == True and hasDigit == True:
                                print("\nPassword has been set!")
                                break
                        else:
                                if hasUpper == False:
                                        print(f"Password must have alteast 1 upper case letter")
                                if hasSpecialSymbol == False:
                                        print(f"Password must have alteast 1 special symbol (_, !, @, #, $, %, &)")
                                if hasDigit == False:
                                        print(f"Password must have at least 1 number")
                else:
                        print(f"Pasword must be at least 8 characters long")


        # Hashing all the inputs for security
        email = hashlib.sha512(email.encode("utf-8")).hexdigest()
        pswrd = hashlib.sha512(pswrd.encode("utf-8")).hexdigest()


        credDict = {
                "id": id,
                "name": name,
                "email": email,
                "pswrd": pswrd,
                "studData":{}
        }

        with open(f"data/{id}.json", "w") as file:
                file.write("{}")
        
        with open(f"data/{id}.json", "r") as file:
                data = json.load(file)

        data = credDict

        with open(f"data/{id}.json", "w") as file:
                json.dump(data, file, indent = 8)




def signIn():
        pass




while True:
        selector = input("Enter your choice from the above list (EXCEEDING VALUES WILL BE CLIPPED TO NEAREST LIMIT): ")

        try:
                selector = int(selector)

                if selector < 1:
                        selector = 1
                elif selector > 2:
                        selector = 2

                break
        except ValueError or EOFError:
                print("Invalid Input\n")

if selector == 1:
        print("\n\nSIGN UP AS AN INSTITUTE")
        print    ("-----------------------\n")

        signUp()
else:
        print("\n\nSIGN IN")
        print    ("-------\n")

        signIn()
