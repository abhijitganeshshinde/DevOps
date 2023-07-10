choice = int(input(" 1. Addition\n 2. Subtraction\n 3. Division\n 4. Multipliction\n Please Select The Above Choice:"))

firstNum = float(input("Enter The First Value :"))
secNum =float(input("Enter The First Value :"))
def addition(firstValue,secValue):
    print("Addition Is ",firstValue + secValue)

def subtraction(firstValue,secValue):
    print("Subtraction Is ",firstValue - secValue)

def division(firstValue,secValue):
    print("Division Is ",firstValue / secValue)

def multipliction(firstValue,secValue):
    print("Multipliction Is ",firstValue * secValue)


if(choice == 1):
    addition(firstNum,secNum)
elif(choice == 2):
    subtraction(firstNum,secNum)
elif(choice == 3):
    division(firstNum,secNum)
elif(choice == 4):
    multipliction(firstNum,secNum)
else:
   print("Wrong Input")



