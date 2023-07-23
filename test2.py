def add_product(category: str, product: str) -> None:
    category_list: list = products.get(category, [])
    for item in category_list:
        if item["name"] == product:
    item["quantity"] -= 1
            basket.append(item)
            break
    else:
        print("we haven't this product")


category = input("category: ").title()
product_name= input("Enter ur item: ").lower()
add_product(category, product_name)  
print(basket)