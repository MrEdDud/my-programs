import numexpr

def calculate(expression):
    try:
        return numexpr.evaluate(expression)
    except (SyntaxError, ValueError):
        return None

calculcation = input("Enter what you would like to calculate\n> ")
result = calculate(calculcation)
print(f"Result: {result}")