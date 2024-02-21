print("Welcome to Our Restaurant!\n")

# Menu dictionary containing items and their prices
menu = {
    "1": {"item": "Burger", "price": 10.99},
    "2": {"item": "Pizza", "price": 12.99},
    "3": {"item": "Pasta", "price": 9.99},
    "4": {"item": "Salad", "price": 6.99},
    "5": {"item": "Soup", "price": 4.99}
}

# Display menu
print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['item']}: {value['price']}/-")

# Initialize empty list to store selected items
selected_items = []

# Get user input for selected items
while True:
    choice = input("\nEnter the number of the item you'd like to order (press 'done' to finish): ")
    if choice.lower() == "done":
        break
    elif choice in menu:
        selected_items.append(menu[choice])
    else:
        print("Invalid choice. Please try again.")

# Calculate total bill
total_bill = sum(item['price'] for item in selected_items)

# Display bill
print("\nYour Bill:")
for item in selected_items:
    print(f"{item['item']}: {item['price']}/-")
print(f"Total: ${total_bill}")

# Ask for a tip
tip = input("\nWould you like to add a tip? (yes/no): ")
if tip.lower() == "yes":
    tip_amount = float(input("Enter the tip amount ($): "))
    total_bill += tip_amount

# Thank you message
print("\nThank you for dining with us! We hope to see you again soon!")
