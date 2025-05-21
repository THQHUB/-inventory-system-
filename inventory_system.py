inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[name] = {'quantity': quantity, 'price': price}
    print(f"Item '{name}' added successfully.")

def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[name] = {'quantity': quantity, 'price': price}
        print(f"Item '{name}' updated.")
    else:
        print("Item not found.")

def delete_item():
    name = input("Enter item name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' deleted.")
    else:
        print("Item not found.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for name, details in inventory.items():
            print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

def main():
    while True:
        print("\n1. Add Item\n2. Update Item\n3. Delete Item\n4. View Inventory\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
