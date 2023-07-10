num = int(input("Enter an integer: "))
if(num != 0):
    num += 1
    for i in range(1, num):
        spaces = " " * (num - i)
        stars = "*" * (2*i - 1)
        print(spaces + stars)