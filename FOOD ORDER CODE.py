#Customer Name input
print("What is your name?")
name = input("")

# Menu items with prices
menu = {
    1: {"item": "Burger and Chips", "price": 29.99},
    2: {"item": "Fish and Chips", "price": 19.99},
    3: {"item": "Hotdog and Chips", "price": 24.99}
}

# Initialize the order list
order = []

more_items = 'yes'
while more_items == 'yes':
    choice = int(input("\nWhat would you like to order (1-3)? "))
    quantity = int(input("How much quantity would you like? "))

    if 1 <= choice <= 3:
        item = menu[choice]['item']
        price = menu[choice]['price']
        total_cost = price * quantity
        print("You have selected " + str(quantity) + " " + item + "(s) for $" + str(total_cost) + ".")
        order.append({"item": item, "quantity": quantity, "total_cost": total_cost})
    else:
        print("Invalid selection. Please choose a valid item number (1-3).")

    more_items = input("Do you want to order more items (yes/no)? ").lower()

# Calculate the total cost of the order
if order:
    total = sum(item['total_cost'] for item in order)
    print("Your order list:")
    for item in order:
        print(str(item['quantity']) + " " + item['item'] + " - $" + str(item['total_cost']))
    print("Total cost: $" + str(total))
    print("\nThank you for ordering, " + name + "!")
else:
    print("No items were ordered. Thank you for considering our menu.")