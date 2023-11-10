# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input(f"\nEnter the item number from the {menu_category_name} menu: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)
                
                # 4. Check if the menu selection is in the menu items               
                if menu_selection in menu_items.keys():
                    
                    # Store the item name as a variable
                    selected_item = menu_items[menu_selection]

                    # Ask the customer for the quantity of the menu item
                    quantity_input = input(f"\nEnter how many of the item from the {menu_category_name} menu you want: ")
                    
                    # Check if the quantity is a number, default to 1 if not
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Invalid quantity. Please enter a positive quantity.")
                        else:
                            # Add the item name, price, and quantity to the order list                            
                            order.append({
                                "Item Name": selected_item['Item name'],
                                "Price": selected_item['Price'],
                                "Quantity": quantity
                            })
                            print(f"\n{quantity} {selected_item['Item name']} added to your order.")
                    else:
                        # Default to quantity of 1 if the user doesn't provide a valid quantity
                        quantity = 1
                        # Add the item name, price, and quantity to the order list                            
                        order.append({
                            "Item Name": selected_item['Item name'],
                            "Price": selected_item['Price'],
                            "Quantity": quantity
                        })
                        print(f"\n{quantity} {selected_item['Item name']} added to your order.")
                else:
                    print("Invalid menu item number. Please enter a valid number.")
            else:
                # Tell the customer that their input isn't valid
                print("Invalid input. Please enter a valid number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

    # Check the customer's input
    if keep_ordering.lower() == 'n':
        # Exit the keep ordering question loop and complete the order
        place_order = False
        print("\nThank you for your order!")

# Print out the customer's order
print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order
for item in order:
    # Store the dictionary items as variables
    item_name = item['Item Name']
    item_price = item['Price']
    quantity = item['Quantity']

    # Calculate the number of spaces for formatted printing
    name_spaces = 26 - len(item_name)
    price_spaces = 2
    quantity_spaces = 10

    # Create space strings
    name_space_string = " " * name_spaces
    price_space_string = " " * price_spaces
    quantity_space_string = " " * quantity_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{name_space_string}| ${item_price:.2f}{price_space_string}| {quantity}{quantity_space_string}")

# Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum() and print the prices.
total_cost = sum(item['Price'] * item['Quantity'] for item in order)
print("\nTotal Cost: $" + str(total_cost))
