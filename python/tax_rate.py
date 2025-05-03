#Question: Calculate someones income tax depending on their income
#Inputs their salary
salary = int(input("How much money did you make this year? "))

#Checks if the salary is under 0
if salary < 0:
    print("Error: out of bounds")
    #Calculates the tax rate that the user would have
else:
    if salary > 100001:
        taxRate = 0.3
    elif salary > 50001 and salary < 100000:
        taxRate = 0.25
    elif salary > 10001 and salary < 50000:
        taxRate = 0.15
    elif salary > 0 and salary < 10000:
        taxRate = 0.1

#Calculates how much tax needs to be payed
taxAmount = salary*taxRate

#Outputs how much tax needs to be payed and their taxed income
print("You have to pay £",taxAmount,"in taxes")
print("Your taxed income is £",(salary-taxAmount))