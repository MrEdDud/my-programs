def diamond(num):
    for x in range(num):
        print(" " * (num - x - 1) + "*" * (2 * x + 1))

    for x in range(num - 2, -1, -1):
        print(" " * (num - x - 1) + "*" * (2 * x + 1))

while True:
    diamond(10)