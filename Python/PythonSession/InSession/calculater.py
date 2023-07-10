# choice = int(input(" 1. Addition\n 2. Subtraction\n 3.Division\n 4.Multipliction\n Please Select The Above Choice:"))

# firstNum = int(input("Enter The First Value :"))
# secNum =int(input("Enter The First Value :"))
# ans=''
# if(choice == 1):
#     ans = firstNum + secNum
#     print("Addition Is ",ans)
# elif(choice == 2):
#     ans = firstNum - secNum
#     print("Subtraction Is ",ans)
# elif(choice == 3):
#     ans = firstNum/secNum
#     print("Division Is ",ans)
# elif(choice == 4):
#     ans = firstNum*secNum
#     print("Multipliction Is ",ans)
# else:
#    print("Wrong Input")




valid_choice = False

while not valid_choice:
    choice = input(" 1. Addition\n 2. Subtraction\n 3. Division\n 4. Multiplication\n Please Select One of the Above Choices: ")

    try:
        choice = int(choice)
        if choice < 1 or choice > 4:
            raise ValueError
        valid_choice = True
    except ValueError:
        print("Invalid input! Please enter a valid integer choice between 1 and 4.")

firstNum = input("Enter the First Value: ")
secNum = input("Enter the Second Value: ")

try:
    firstNum = float(firstNum)
    secNum = float(secNum)
except ValueError:
    print("Invalid input! Please enter valid numeric values.")
    exit()

if choice == 1:
    ans = firstNum + secNum
    print("Addition Is", ans)
elif choice == 2:
    ans = firstNum - secNum
    print("Subtraction Is", ans)
elif choice == 3:
    if secNum == 0:
        print("Cannot divide by zero!")
        exit()
    ans = firstNum / secNum
    print("Division Is", ans)
elif choice == 4:
    ans = firstNum * secNum
    print("Multiplication Is", ans)
else:
    print("Wrong Input")
