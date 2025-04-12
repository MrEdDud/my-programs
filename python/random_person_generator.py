# Importing modules
import random

# Creating a list to store the alphabet in capital letters
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Declaring variables
loop = True

# Creating a function called menu
def menu():
    loop = True

    while loop:
        print("+-"*20+"+")
        print('''Welcome! Which option would you like?
1. Random Email
2. Random Phone number
3. Random National Insurance number
4. Exit''')
        
        choice = input("Enter a number: ")

        try:
            int(choice)
        except:
            print("Error: Enter a number!")
            loop = True
        else:
            if int(choice) < 1 or int(choice) > 4:
                print("Error: Enter a valid choice!")
                loop = True
            else:
                print("+-"*20+"+")
                return int(choice)

# Creating a function called amount
def amount():
    loop = True

    while loop:
        amount = input("> ")

        try:
            int(amount)
            return int(amount)
        except:
            print("Error: Enter a number!")
            loop = True

# Creating a function called emails
def emails():
    start = ['Jeremy','Timmy']
    middle = ['Jake','Thompson']
    end = ['Gervais','Holland']
    email = ['@gmail.com','@yahoo.com']
    num_list = [str(random.randint(0,9)) for x in range(random.randint(0,6))]

    num = ''.join(num_list)

    print(f"{random.choice(start)}{random.choice(middle)}{random.choice(end)}{num}{random.choice(email)}")

# Creating a function called phone_num
def phone_num():
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    num4 = random.randint(0,9)
    num5 = random.randint(0,9)
    num6 = random.randint(0,9)
    num7 = random.randint(0,9)
    num8 = random.randint(0,9)
    num9 = random.randint(0,9)

    print(f"07{num1}{num2}{num3} {num4}{num5}{num6}{num7}{num8}{num9}")

# Creating a function called national insurance number
def national_insurance_number():
    item1 = random.choice(list(alphabet))
    item2 = random.choice(list(alphabet))
    item3 = random.randint(0,9)
    item4 = random.randint(0,9)
    item5 = random.randint(0,9)
    item6 = random.randint(0,9)
    item7 = random.randint(0,9)
    item8 = random.randint(0,9)
    item9 = random.choice(list(alphabet))

    print(f"{item1}{item2} {item3}{item4} {item5}{item6} {item7}{item8} {item9}")

# Creating a function called return_to_menu
def return_to_menu():
    loop = True

    while loop:
        print("Return to menu?")
        item = input("> ")

        if item == "yes" or item == "no":
            return item
        else:
            print("Error: Enter yes or no!")
            loop = True


while loop:
    main_menu = menu()
    # Menu option 1
    if main_menu == 1:
        print("How many emails would you like?")
        quantity = amount()
        for x in range(quantity):
            emails()
        return_menu = return_to_menu()
        if return_menu != "yes":
            print("Goodbye!\n")
            loop = False
        else:
            loop = True
    # Menu option 2
    elif main_menu == 2:
        print("How many phone numbers would you like?")
        quantity = amount()
        for x in range(quantity):
            phone_num()
        return_menu = return_to_menu()
        if return_menu != "yes":
            print("Goodbye!\n")
            loop = False
        else:
            loop = True
    # Menu option 3
    elif main_menu == 3:
        print("How many N.I numbers would you like?")
        quantity = amount()
        for x in range(quantity):
            national_insurance_number()
        return_menu = return_to_menu()
        if return_menu != "yes":
            print("Goodbye!\n")
            loop = False
        else:
            loop = True
    # Menu option 4
    else:
        print("Goodbye!\n")
        break