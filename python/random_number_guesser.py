import random

random_number = random.randint(0,10)
loop = True

if random_number%2 == 0:
    hint = "Your number is even!"
else:
    hint = "Your number is odd!"

random_number = str(random_number)

while loop:
    num = input("Enter a number: ")

    if num == random_number:
        print("You got the correct number!")
        loop = False
    elif num.lower() == "hint":
        print(hint)
    else:
        print("Try again!")