"""
TURN LINE WRAPPING OFF FOR A BETTER VIEW

+-------------------------------------------------------------------+
|            ***------------   MODULE   ------------***             |
|                                                                   |
|                                                                   |
|Author: Raktimjyoti Sarma (RaktimJS)                               |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date Created: 09/03/2025                                           |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
| Contains code that work as UI elements in 'script.py'.            |
+-------------------------------------------------------------------+

Last Edited: 30th March, 2025

"""




import os
import ReadUpdateDelete as rud
from addNewStudent import addNewStudent

DEL_LINE = "\033[A\033[K"
WHITE = "\033[38;2;212;212;212m"
YELLOW = "\033[38;2;255;200m"
RED = "\033[38;2;200;0m"
lb = "\033[38;2;108;180;238m"

isQuitting = True




def ui(schoolID: str, jsonFileName: str):
        os.system('cls')

        grade = int(jsonFileName.split("grade")[1].split(".json")[0])

        while True:
                print(f"\n\n{lb}CLASS {grade}{WHITE}")

                print(f"\n\n{'-'*90}\n\n")

                print(f"Enter {YELLOW}1{WHITE} to SEE BASIC STUDENT DETAILS")
                print(f"Enter {YELLOW}2{WHITE} to SEE EXAM DETAILS OF THE WHOLE CLASS")
                print(f"Enter {YELLOW}3{WHITE} to SEE EXAM DETAILS FOR ONE SUBJECT OF THE WHOLE CLASS")
                print(f"Enter {YELLOW}4{WHITE} to ADD A NEW STUDENT")
                print(f"Enter {YELLOW}5{WHITE} to UPDATE STUDENT'S NAME")
                print(f"Enter {YELLOW}6{WHITE} to UPDATE STUDENT'S MARKS")
                print(f"Enter {YELLOW}7{WHITE} to DELETE A STUDENT'S RECORD\n")
                print(f"{YELLOW}IRREVERSIBLE ACTION:{WHITE}")
                print(f"Enter {YELLOW}8{WHITE} to {RED}DELETE ALL RECORDS{WHITE}\n\n")

                print(f"TYPE '{YELLOW}QUIT{WHITE}' TO QUIT")

                operationSelector = input(f"\n\nEnter your choice from the above list: {YELLOW}")
                print(WHITE, end="")

                operationSelector.replace(" ","")

                if operationSelector.lower() == 'quit':
                        print("\nTHANK YOU!")

                        isQuitting = True

                        break
                elif operationSelector.lower() != "quit" and operationSelector not in '12345678':
                        print("Invalid Input. Try again")
                        isQuitting = False
                elif not operationSelector.strip() == True and operationSelector not in '12345678':
                        print("Invalid Input. Try again")
                        isQuitting = False
                else:
                        isQuitting = False
                        operationSelector = int(operationSelector)

                        if operationSelector == 1:
                                print(f"\n\n{'-'*70}\n\n")

                                rud.printGradeData(schoolID, jsonFileName, grade, True)
                        elif operationSelector == 2:
                                print(f"\n\n{'-'*70}\n\n")

                                rud.printGradeData(schoolID, jsonFileName, grade, False)
                        elif operationSelector == 3:
                                print(f"\n\n{'-'*70}\n\n")

                                subject = input(f"Enter the subject you want to view marks for: {YELLOW}")
                                print(WHITE, end="")

                                rud.printGradeData(schoolID, jsonFileName, grade, False, subject)
                        elif operationSelector == 4:
                                print(f"\n\n{'-'*70}\n\n")

                                addNewStudent(schoolID, jsonFileName)
                        elif operationSelector == 5:
                                print(f"\n\n{'-'*70}\n\n")

                                while True:
                                        try:
                                                rollNumber = input(f"Enter roll no. of the student whose name is to be edited: {YELLOW}")
                                                print(WHITE, end="")

                                                rollNumber = int(rollNumber)

                                                break
                                        except ValueError or EOFError:
                                                print("Invalid Input\n")

                                newName = input(f"Enter the new name: {YELLOW}")
                                print(WHITE, end="")

                                rud.updateName(schoolID, jsonFileName, rollNumber, newName)
                                rud.printSpecificStudent(schoolID, jsonFileName, rollNumber)
                        elif operationSelector == 6:
                                print(f"\n\n{'-'*70}\n\n")

                                while True:
                                        try:
                                                rollNumber = input(f"Enter roll no. of the student whose mark(s) is(are) to be edited: {YELLOW}")
                                                print(WHITE, end="")

                                                rollNumber = int(rollNumber)

                                                break
                                        except ValueError or EOFError:
                                                print("Invalid Input\n")

                                rud.updateMarks(schoolID, jsonFileName, rollNumber)
                        elif operationSelector == 7:
                                print(f"\n\n{'-'*70}\n\n")

                                while True:
                                        try:
                                                rollNumber = input(f"Enter roll no. of the student whose data is to be deleted: {YELLOW}")
                                                print(WHITE, end="")

                                                rollNumber = int(rollNumber)

                                                break
                                        except ValueError or EOFError:
                                                print("Invalid Input\n")
                                        
                                rud.deleteRecord(schoolID, jsonFileName, rollNumber)
                        elif operationSelector == 8:
                                print(f"\n\n{'-'*70}\n\n")

                                rud.clearGradeData(schoolID, jsonFileName)



