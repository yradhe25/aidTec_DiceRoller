import random

print("Welcome to the Dice Roller!")
def roll_dice():
    while(True):
        dice1=input("Enter the number of dice to roll or 0 to quit : ")

        try:
            dice=int(dice1)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if dice==0:
            print("Thank You for using the Dice Roller. Goodbye!")
            break
        
        elif dice>0:
            print("The numbers are : ")
            for i in range(dice):
                numbers=random.randint(1,6)
                print(numbers)
            roll_again=input("Do you want to roll the dice again? ( Y/N ) : ")
            
            if roll_again=="Y" or roll_again=="y":
                continue

            elif roll_again=="N" or roll_again=="n":
                print("Thank You for using the Dice Roller. Goodbye!")
                break

        else:
            print("Please enter a valid number!")
        

roll_dice()