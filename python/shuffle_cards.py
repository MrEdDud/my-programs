import random

card_num = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
card_symbol = ["Spades","Hearts","Diamonds","Clubs"]

amount = int(input("How many cards would you like? (Max 15)\n> "))

while amount > 15 or amount <= 0:
    print("Error: Too many cards!")
    amount = int(input("How many cards would you like? (Max 15)\n> "))

for x in range(amount):
    card = random.choice(card_symbol)
    card_number = random.choice(card_num)
    print(f"Card {x+1}: {card_number} of {card}")