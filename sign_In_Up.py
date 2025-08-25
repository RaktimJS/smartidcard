import os, hashlib, json, datetime
from pathlib import Path

from schoolDashboard import entry

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
        print("Your school ID is:", id, "\n")

        # Email -------------------
        while True:
                email = input("Enter your email: ")

                if email.count("@") == 1:
                        username = email[:email.index("@")]

                        if len(username) > 0:
                                domain = email[email.index("@") + 1:]

                                if domain.count(".") == 1:
                                        tld = domain[domain.index(".") + 1:]

                                        if len(tld) > 0:
                                                domainName = domain[:domain.index(".")]

                                                if len(domainName) > 0:
                                                        break
                                                else:
                                                        print("Invalid Input\n")
                                        else:
                                                print("Invalid input\n")
                                else:
                                        print("Invalid input\n")
                        else:
                                print("Invalid input\n")
                else:
                        print("Invalid input\n")

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


        # Hashing inputs for security
        pswrd = hashlib.sha512(pswrd.encode("utf-8")).hexdigest()


        # Create a new set of JSON files for every new sign up
        base = Path(__file__).parent / "data" / f"{id}"

        (base / "academic").mkdir(parents=True, exist_ok=True)
        (base / "cocurricular").mkdir(parents=True, exist_ok=True)
        (base / "health").mkdir(parents=True, exist_ok=True)

        for i in range(12):
                (base / "academic" / f"grade{i+1}.json").write_text("{}")
                (base / "cocurricular" / f"grade{i+1}.json").write_text("{}")
                (base / "health" / f"grade{i+1}.json").write_text("{}")


        '''
        Appending the data details of the newly registered
        school in `mapping.json` for mapping and granting
        access upon sign up
        '''
        with open("mapping.json", "r") as mapFile:
                data = json.load(mapFile)

        data.append(
                {
                        "id": id,
                        "email": email,
                        "pswrd": pswrd,
                        "name": name
                }
        )

        with open("mapping.json", "w") as mapFile:
                data = json.dump(data, mapFile, indent = 8)


def signIn():
        print("Enter 1 to sign in as an institute")
        print("Enter 2 to sign in as a student")

        while True:
                selector = input("\nEnter your choice from the above list (EXCEEDING VALUES WILL BE CLIPPED TO NEAREST LIMIT): ")

                try:
                        selector = int(selector)

                        if selector < 1:
                                selector = 1
                        elif selector > 2:
                                selector = 2

                        break
                except ValueError or EOFError:
                        print("Invalid Input\n")

        grantAccess = False

        if selector == 1:
                print("\n\nSIGN IN AS AN INSTITUTE")
                print("-----------------------\n")

                id = input("Enter school email or school ID: ")
                pswrd = input("Enter password: ")

                pswrd = hashlib.sha512(pswrd.encode("utf-8")).hexdigest()

                with open("mapping.json", "r") as mapFile:
                        mapFileData = json.load(mapFile)

                if "@" in id:
                        for i in mapFileData:
                                if i["email"] == id and i["pswrd"] == pswrd:
                                        grantAccess = True
                                        name = i["name"]
                                        id = i["id"]
                                        break
                else:
                        for i in mapFileData:
                                if i["id"] == id and i["pswrd"] == pswrd:
                                        grantAccess = True
                                        name = i["name"]
                                        id = i["id"]
                                        break

                if grantAccess == True:
                        os.system("cls")
                        print(f"{name.upper()} ID: {id}\n", sep="")
                        entry()
                else:
                        print("Invalid Credentials")
        else:
                print("\n\nSIGN IN AS A STUDENT")
                print("--------------------\n")




if __name__ == "__main__":
        print()
        print("Enter 1 to sign up (as an institute)")
        print("Enter 2 to sign in\n")

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
