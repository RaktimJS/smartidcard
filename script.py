# Academic Data Management System

from os import system
from functionControl import ui, isQuitting as iq

system("cls")




def acadDataMngr(schoolID: str):
        breakAll = False

        # try:
        DEL_LINE = "\033[A\033[K"
        WHITE = "\033[38;2;212;212;212m"
        YELLOW = "\033[38;2;255;200m"
        RED = "\033[38;2;200;0m"
        lb = "\033[38;2;108;180;238m"
        LIGHT_YELLOW = "\033[38;2;255;224;110m"

        B = "\033[1m"
        R = "\033[0m"

        continuationSelector = ''

        while True:
                if (continuationSelector == 'cls' or continuationSelector == ''):
                        print("\n")

                        print(f"Enter  {lb}1{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}1{WHITE}")
                        print(f"Enter  {lb}2{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}2{WHITE}")
                        print(f"Enter  {lb}3{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}3{WHITE}")
                        print(f"Enter  {lb}4{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}4{WHITE}")
                        print(f"Enter  {lb}5{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}5{WHITE}")
                        print(f"Enter  {lb}6{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}6{WHITE}")
                        print(f"Enter  {lb}7{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}7{WHITE}")
                        print(f"Enter  {lb}8{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}8{WHITE}")
                        print(f"Enter  {lb}9{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade  {YELLOW}9{WHITE}")
                        print(f"Enter {lb}10{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}10{WHITE}")
                        print(f"Enter {lb}11{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}11{WHITE}")
                        print(f"Enter {lb}12{WHITE} {LIGHT_YELLOW}→{WHITE} Access Grade {YELLOW}12{WHITE}\n")

                        print(f"\n{RED}Any exceeding values will be clipped to the closest limit{WHITE}\n")

                        print(f"Type {YELLOW}QUIT{WHITE} to quit\n\n")



                while True:
                        try:
                                listSelector = input(f"Enter your choice: {YELLOW}")
                                print(WHITE, end="")

                                if listSelector.lower() != "quit":
                                        listSelector = int(listSelector)

                                        if listSelector == 1:
                                                ui(schoolID, "grade1.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 2:
                                                ui(schoolID, "grade2.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 3:
                                                ui(schoolID, "grade3.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 4:
                                                ui(schoolID, "grade4.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 5:
                                                ui(schoolID, "grade5.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 6:
                                                ui(schoolID, "grade6.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 7:
                                                ui(schoolID, "grade7.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 8:
                                                ui(schoolID, "grade8.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 9:
                                                ui(schoolID, "grade9.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 10:
                                                ui(schoolID, "grade10.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 11:
                                                ui(schoolID, "grade11.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector == 12:
                                                ui(schoolID, "grade12.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector < 1:
                                                listSelector = 1
                                                ui(schoolID, "grade1.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")
                                        elif listSelector > 12:
                                                ui(schoolID, "grade12.json")
                                                print(f"\n\n{'-'*70}\n\n")
                                                system("cls")

                                        break
                                else:
                                        iq = False
                                        breakAll = True
                                        break
                        except ValueError:
                                if not str(listSelector).strip():
                                        print(f"{DEL_LINE}Enter your choice: {YELLOW}\033[3m*BLANK*\033[0m{WHITE}")
                                        print("Invalid Input\n")
                                else:
                                        print("Invalid Input\n")

                if breakAll == True:
                        break
        # except Exception as e:
        #         print(f"Error: {e}")
        #         input("Press Enter to continue")
