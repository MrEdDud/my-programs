typeItem = ["Too small", "Small letter", "Large letter", "Small package", "Medium package", "Too big"]
maxWeight = [0, 100, 750, 2000, 20000]
x = 0

inWeight = int(input("Enter an item weight "))

while True and x < len(maxWeight):
    if inWeight > maxWeight[x]:
        x += 1
    else:
        break
print(typeItem[x])

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()