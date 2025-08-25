'''
This module contains function(s) to be executed when the user signs in as a school
'''

def academic():
        pass

def extraCurricular():
        pass

def health():
        pass

def entry():
        print("Enter 1 → Access academic data")
        print("Enter 1 → Access extra curricular data")
        print("Enter 1 → Access health data")

        while True:
                listSelector = input("\nEnter your choice: ")

                try:
                        listSelector = int(listSelector)
                        break
                except ValueError or EOFError:
                        print("Invalid Input\n")
        
        if listSelector == 1:
                academic()
        elif listSelector == 2:
                extraCurricular()
        elif listSelector == 3:
                health()
        elif listSelector < 1:
                print("Exceeding value, clipped to 1")
                academic()
        elif listSelector > 3:
                print("Exceeding value, clipped to 3")
                health()
