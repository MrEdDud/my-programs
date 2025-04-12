#Question: Create a grading system
#Inputs the score
score = int(input("How many marks did you get in your test? "))

#Checks if score is more than 100 or less than 0
if score > 100 or score < 0:
    print("Error: score is out of bounds!")
else:
    #Checks which grade they got and then outputs what grade they got
    if score >= 0 and score <= 49:
        print("You got an F!")
    elif score >= 50 and score <= 54:
        print("You got a D!")
    elif score >= 55 and score <= 64:
        print("You got a C!")
    elif score >= 65 and score <= 79:
        print("You got a B!")
    else:
        print("You got an A!")