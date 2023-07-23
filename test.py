basket = []
# Define a dictionary called 'products' that contains four categories of appliances with their respective products
# Each product is represented as a dictionary with a name, price, and quantity
Kitchen_Appliances = [
    {"name": "oven", "price": 500, "quantity": 52},
    {"name": "stove", "price": 700, "quantity": 101},
    {"name": "refrigerator", "price": 1000, "quantity": 23},
    {"name": "microwave", "price": 150, "quantity": 53},
    {"name": "coffee maker", "price": 50, "quantity": 42},
    {"name": "toaster", "price": 30, "quantity": 30},
    {"name": "blender", "price": 60, "quantity": 25},
    {"name": "food processor", "price": 80, "quantity": 23},
    {"name": "dishwasher", "price": 500, "quantity": 42},
    {"name": "hand mixer", "price": 20, "quantity": 152},
    {"name": "slow cooker", "price": 50, "quantity": 14},
    {"name": "air fryer", "price": 100, "quantity": 10},
    {"name": "electric kettle", "price": 40, "quantity": 9},
    {"name": "juicer", "price": 80, "quantity": 87},
    {"name": "rice cooker", "price": 40, "quantity": 0},
    {"name": "stand mixer", "price": 300, "quantity": 1},
    {"name": "waffle maker", "price": 40, "quantity": 12},
    {"name": "panini press", "price": 50, "quantity": 5},
    {"name": "bread maker", "price": 80, "quantity": 4}
]

Cleaning_Appliances = [ 
    {"name": "vacuum cleaner", "price": 200, "quantity": 75},
    {"name": "steam mop", "price": 100, "quantity": 5},
    {"name": "pressure washer", "price": 300, "quantity": 15},
    {"name": "carpet cleaner", "price": 150, "quantity": 125},
    {"name": "air purifier", "price": 150, "quantity": 452},
    {"name": "steam cleaner", "price": 100, "quantity": 45},
    {"name": "handheld vacuum", "price": 50, "quantity": 23},
    {"name": "robotic vacuum", "price": 300, "quantity": 52},
    {"name": "stick vacuum", "price": 100, "quantity": 85},
    {"name": "dustbuster", "price": 30, "quantity": 52},
    {"name": "window cleaner", "price": 50, "quantity": 63},
    {"name": "broom and dustpan", "price": 20, "quantity": 75},
    {"name": "mop and bucket", "price": 30, "quantity": 85},
    {"name": "dust mop", "price": 20, "quantity": 100},
    {"name": "toilet brush", "price": 10, "quantity": 52},
    {"name": "laundry detergent", "price": 15, "quantity": 50},
    {"name": "fabric softener", "price": 10, "quantity": 31},
    {"name": "stain remover", "price": 5, "quantity": 87},
    {"name": "dish soap", "price": 5, "quantity": 19}
]

Laundry_Appliances = [
    {"name": "washing machine", "price": 800, "quantity": 5},
    {"name": "dryer", "price": 600, "quantity": 7},
    {"name": "iron", "price": 40, "quantity": 20},
    {"name": "ironing board", "price": 25, "quantity": 10}
    ]

Heating_Cooling_Appliances =[ 
    {"name": "air conditioner", "price": 1000, "quantity": 3},
    {"name": "fan", "price": 50, "quantity": 10},
    {"name": "space heater", "price": 80, "quantity": 5},
    {"name": "humidifier", "price": 60, "quantity": 8},
    {"name": "dehumidifier", "price": 100, "quantity": 4}
    ]


products = {'Kitchen Appliances': Kitchen_Appliances , "Cleaning Appliances": Cleaning_Appliances,"Laundry Appliances":Laundry_Appliances,
            "Heating Cooling Appliances": Heating_Cooling_Appliances}


# Define a function called 'add_product' that takes in a category and product and adds it to the global 'basket' list
# The function first checks if the category exists in the 'products' dictionary, and returns an error message if it doesn't
# It then searches for the product in the category list, and if it exists, decrements its quantity by 1 and adds it to the basket list
# If the product is out of stock, it returns an error message, and if it doesn't exist in the category, it returns an error message as well


# def add_product(category: str, product: str) -> None:
#     """
#     Adds a product to the global basket list.

#     Parameters:
#     category (str): The category of the product.
#     product (str): The name of the product.

#     Returns:
#     None.
#     """

#     category_list: list = products.get(category, [])
#     if not category_list:
#         print("Invalid category")
#     else:
#         for item in category_list:
#             if item["name"] == product:
#                 if item["quantity"] > 0:
#                     item["quantity"] -= 1
#                     basket.append(item)
#                     print(f"{product} added to basket")
#                 else:
#                     print("This product is out of stock")
#                 break
#         else:
#             print("We don't have this product")

# while True:
#     category = input("Enter the category of the product (or 'done' to finish): ").title()
#     if category == "Done":
#         break
#     product_name = input("Enter the name of the product: ").lower()
#     add_product(category, product_name)
    
# print("Items in basket:")
# if not basket:
#     print("Your basket is empty")
# else:
#     for item in basket:
#         print(item["name"])

















basket = []
# Define a dictionary called 'products' that contains four categories of appliances with their respective products
# Each product is represented as a dictionary with a name, price, and quantity
Kitchen_Appliances = [
    {"name": "oven", "price": 500, "quantity": 52},
    {"name": "stove", "price": 700, "quantity": 101},
    {"name": "refrigerator", "price": 1000, "quantity": 23},
    {"name": "microwave", "price": 150, "quantity": 53},
    {"name": "coffee maker", "price": 50, "quantity": 42},
    {"name": "toaster", "price": 30, "quantity": 30},
    {"name": "blender", "price": 60, "quantity": 25},
    {"name": "food processor", "price": 80, "quantity": 23},
    {"name": "dishwasher", "price": 500, "quantity": 42},
    {"name": "hand mixer", "price": 20, "quantity": 152},
    {"name": "slow cooker", "price": 50, "quantity": 14},
    {"name": "air fryer", "price": 100, "quantity": 10},
    {"name": "electric kettle", "price": 40, "quantity": 9},
    {"name": "juicer", "price": 80, "quantity": 87},
    {"name": "rice cooker", "price": 40, "quantity": 0},
    {"name": "stand mixer", "price": 300, "quantity": 1},
    {"name": "waffle maker", "price": 40, "quantity": 12},
    {"name": "panini press", "price": 50, "quantity": 5},
    {"name": "bread maker", "price": 80, "quantity": 4}
]

Cleaning_Appliances = [ 
    {"name": "vacuum cleaner", "price": 200, "quantity": 75},
    {"name": "steam mop", "price": 100, "quantity": 5},
    {"name": "pressure washer", "price": 300, "quantity": 15},
    {"name": "carpet cleaner", "price": 150, "quantity": 125},
    {"name": "air purifier", "price": 150, "quantity": 452},
    {"name": "steam cleaner", "price": 100, "quantity": 45},
    {"name": "handheld vacuum", "price": 50, "quantity": 23},
    {"name": "robotic vacuum", "price": 300, "quantity": 52},
    {"name": "stick vacuum", "price": 100, "quantity": 85},
    {"name": "dustbuster", "price": 30, "quantity": 52},
    {"name": "window cleaner", "price": 50, "quantity": 63},
    {"name": "broom and dustpan", "price": 20, "quantity": 75},
    {"name": "mop and bucket", "price": 30, "quantity": 85},
    {"name": "dust mop", "price": 20, "quantity": 100},
    {"name": "toilet brush", "price": 10, "quantity": 52},
    {"name": "laundry detergent", "price": 15, "quantity": 50},
    {"name": "fabric softener", "price": 10, "quantity": 31},
    {"name": "stain remover", "price": 5, "quantity": 87},
    {"name": "dish soap", "price": 5, "quantity": 19}
]

Laundry_Appliances = [
    {"name": "washing machine", "price": 800, "quantity": 5},
    {"name": "dryer", "price": 600, "quantity": 7},
    {"name": "iron", "price": 40, "quantity": 20},
    {"name": "ironing board", "price": 25, "quantity": 10}
    ]

Heating_Cooling_Appliances =[ 
    {"name": "air conditioner", "price": 1000, "quantity": 3},
    {"name": "fan", "price": 50, "quantity": 10},
    {"name": "space heater", "price": 80, "quantity": 5},
    {"name": "humidifier", "price": 60, "quantity": 8},
    {"name": "dehumidifier", "price": 100, "quantity": 4}
    ]


products = {'Kitchen Appliances': Kitchen_Appliances , "Cleaning Appliances": Cleaning_Appliances,"Laundry Appliances":Laundry_Appliances,
            "Heating Cooling Appliances": Heating_Cooling_Appliances}


# Define a function called 'add_product' that takes in a category and product and adds it to the global 'basket' list
# The function first checks if the category exists in the 'products' dictionary, and returns an error message if it doesn't
# It then searches for the product in the category list, and if it exists, decrements its quantity by 1 and adds it to the basket list
# If the product is out of stock, it returns an error message, and if it doesn't exist in the category, it returns an error message as well


def add_product(category: str, product: str) -> None:
    """
    Adds a product to the global basket list.

    Parameters:
    category (str): The category of the product.
    product (str): The name of the product.

    Returns:
    None.
    """

    category_list: list = products.get(category, [])
    if not category_list:
        print("Invalid category")
    else:
        for item in category_list:
            if item["name"] == product:
                if item["quantity"] > 0:
                    item["quantity"] -= 1
                    basket.append(item)
                    print(f"{product} added to basket")
                else:
                    print("This product is out of stock")
                break
        else:
            print("We don't have this product")

def remove_product(product_name: str) -> None:
    """
    Removes all products with a given name from the global basket list.

    Parameters:
    product_name (str): The name of the product to remove.

    Returns:
    None.
    """

    i = 0
    while i < len(basket):
        item = basket[i]
        if item["name"] == product_name:
            item["quantity"] += 1
            basket.remove(item)
            print(f"{product_name} removed from basket")
        else:
            i += 1
    if i == 0:
        print(f"{product_name} not found in basket")

def search_product(product_name: str) -> None:
    """
    Searches for all products with a given name in the global product list.

    Parameters:
    product_name (str): The name of the product to search for.

    Returns:
    None.
    """

    found = False
    for category, category_list in products.items():
        for item in category_list:
            if item["name"] == product_name:
                found = True
                print(f"{item['name']} - {category} ({item['price']} dollars)")
    if not found:
        print(f"{product_name} not found")

def show_help() -> None:
    """
    Displays a list of available commands and their descriptions.

    Parameters:
    None.

    Returns:
    None.
    """

    print("Available commands:")
    print("1. Add product to basket - Adds a product to the basket.")
    print("2. Remove product from basket - Removes a product from the basket.")
    print("3. Search for a product - Searches for a product in the list of products.")
    print("4. View list of products - Displays a list of all available products.")
    print("5. View basket - Displays the items currently in the basket.")
    print("6. Change item priority - Changes the priority of an item in the basket.")
    print("7. Exit - Exits the program.")

def display_basket() -> None:
    """
    Displays the items in the basket as a list.

    Parameters:
    None.

    Returns:
    None.
    """

    if not basket:
        print("Your basket is empty")
    else:
        print("Items in basket:")
        for i, item in enumerate(basket, 1):
            print(f"{i}. {item['name']} - {item['price']} dollars")

def change_priority(item_index: int, new_index: int) -> None:
    """
    Changes the priority of an item in the basket.

    Parameters:
    item_index (int): The current index of the item to move.
    new_index (int): The new index to move the item to.

    Returns:
    None.
    """

    if item_index < 1 or item_index > len(basket):
        print("Invalid item index")
    elif new_index < 1 or new_index > len(basket):
        print("Invalid new index")
    else:
        item = basket.pop(item_index - 1)
        basket.insert(new_index - 1, item)
        print(f"{item['name']} moved to position {new_index}")

while True:
    print("1. Add product to basket")
    print("2. Remove product from basket")
    print("3. Search for a product")
    print("4. View list of products")
    print("5. View basket")
    print("6. Change item priority")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Available categories:")
        for category in products:
            print(f"- {category}")
        category = input("Enter the category of the product: ").title()
        product_name = input("Enter the name of the product: ").lower()
        add_product(category, product_name)
        print()

    elif choice == '2':
        product_name = input("Enter the name of the product to remove: ")

        remove_product(product_name)
        print()

    elif choice == '3':
        product_name = input("Enter the name of the product to search for: ").lower()
        search_product(product_name)
        print()

    elif choice == '4':
        print("List of products:")
        for category, category_list in products.items():
            print(category)
            for item in category_list:
                print(f"\t{item['name']} - {item['price']} dollars ({item['quantity']} available)")
        print()

    elif choice == '5':
        display_basket()
        print()

    elif choice == '6':
        item_index = int(input("Enter the current index of the item to move: "))
        new_index = int(input("Enter the new index to move the item to: "))
        change_priority(item_index, new_index)
        print()

    elif choice == '7':
        break

    else:
        print("Invalid choice")
        print()