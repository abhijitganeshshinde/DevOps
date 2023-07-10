menu = {
    1: {"name": "Matar Paneer", "price": 400},
    2: {"name": "Biryani", "price": 450},
    3: {"name": "Pulao", "price": 300}
}

selected_items = []

while True:
    print("Menu:")
    print("---------|-----------------------------------")
    print("  Item   | Name              Price(Rs.)      ")
    print("---------|-----------------------------------")
    for item_id, item in menu.items():
        print(f"   {item_id}     |   {item['name']:15s} {item['price']:4d}")

    choice = input("Enter the item number (0 to finish): ")
    if choice == "0":
        break

    try:
        choice = int(choice)
        if choice in menu:
            selected_items.append(menu[choice])
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")

total_price = sum(item['price'] for item in selected_items)

print("---------------------------")
print("Selected Items:")
print("----------------------------")
for item in selected_items:
    print(f"{item['name']} -- {item['price']}")

print("---------------------------")
print("Total Price:", total_price)

tax = input("Enter tax amount (optional): ")
if tax:
    try:
        tax = float(tax)
        total_price_with_tax = total_price + (total_price * tax / 100)
        print("Total Price (including tax):", total_price_with_tax)
    except ValueError:
        print("Invalid tax amount. Tax calculation skipped.")
else:
    print("Tax calculation skipped.")
