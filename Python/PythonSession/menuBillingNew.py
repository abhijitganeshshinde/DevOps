print("Menu:")
choice = int(input(" 1. Matar Paneer Price -- 400\n 2. Biryani Price -- 450\n 3. Pulao Price -- 300\n Please Select The Above Item: "))

sum = 0
menu = ''
selectedItem = True

while selectedItem:
    if choice == 1:
        sum += 400
        menu += "Matar Paneer Price -- 400\n"
        print("Selected Matar Paneer")
    elif choice == 2:
        sum += 450
        menu += "Biryani Price -- 450\n"
        print("Selected Biryani")
    elif choice == 3:
        sum += 300
        menu += "Pulao Price -- 300\n"
        print("Selected Pulao")
    elif choice == 0:
        selectedItem = False
        print("Total Amount:", sum)
    else:
        print("Wrong Input")

    if selectedItem:
        choice = int(input("Please Select Another Item (0 to finish): "))

print("\nSelected Menu:")
print(menu)
