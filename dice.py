import random
import time

run = True

min = 1
max = 6

while run == True:
    print(("Roll the dice?(Y/N)"))
    choice = str(input('Enter here: '))

    if choice == "Y" or choice == "y":
        print("Rolling...")
        time.sleep(0.5)
        roll = random.randrange(min, max)
        print("You got a ", roll)
    

    elif choice == "N" or choice =="n":
        print("Exiting the program")
        run = False
    else:
        print("Invalid Input.")
        break
        exit()