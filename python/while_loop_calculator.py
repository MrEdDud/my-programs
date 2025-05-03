loop = True

while loop == True:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    operator = input("Operator: ")

    if operator == "+":
        sum = num1+num2
    elif operator == "-":
        sum = num1-num2
    elif operator == "*":
        sum = num1*num2
    elif operator == "**":
        sum = num1**num2
    elif operator == "/":
        sum = num1/num2
    elif operator == "//":
        sum = num1//num2
    elif operator == "%":
        sum = num1%num2
    
    print(f"The total sum is {sum}")

    loop = input("Another calculation? ")
    if loop.lower() == "yes":
        loop = True
    else:
        print("Bye!")
        loop = False