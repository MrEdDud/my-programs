#Question: Create a program for a book store which applies a 10% discount if they get 5 books and a 5% discount if their total is £50 or more
#Inputs the amount of books the user got and the total price
bookAmount = int(input("How many books did you get? "))
totalPrice = int(input("What is your total? "))

#Declares the variable discount
discount = 0

#Checks if the user got 5 books
if bookAmount == 5:
    discount += 0.1

#Checks if the user spent £50 or more
if totalPrice >= 50:
    discount += 0.05

#Calculates the discounted price
discountedPrice = totalPrice - (totalPrice * discount)

#Outputs the percentage of discount the got and their new total price
print(f"You got a {discount*100}% discount")
print(f"Your new total price is £{discountedPrice}")