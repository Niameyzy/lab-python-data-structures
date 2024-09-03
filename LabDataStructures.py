# 1 Define a list called products that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".
products=["t-shirt", "mug", "hat", "book", "keychain"]
print(products)

# 2 Create an empty dictionary called inventory
inventory={}

# 3 Ask the user to input the quantity of each product available in the inventory. Use the product names from the products list as keys in the inventory dictionary and assign the respective quantities as values
inventory["t-shirt"]=int(input("enter a quantity of t-shirt: "))
inventory["mug"]=int(input("enter a quantity of mug: "))
inventory["hat"]=int(input("enter a quantity of hat: "))
inventory["book"]=int(input("enter a quantity of book: "))
inventory["keychain"]=int(input("enter a quantity of keychain: "))
print(inventory)

# 4 Create an empty set called customer_orders
customer_orders=set()
print(type(customer_orders))

# 5 Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the customer_orders set.
# 6 Print the products in the customer_orders set.
i=3
while i>0:
    print("you have "+ str(i) +" choices to do please !")
    customers_choice = input("make a choice from this products list: " + str(products)+ "\n")
    customer_orders.add(customers_choice)
    i-=1
print(customer_orders)
print(type(customer_orders))
# 7 Calculate the following order statistics:
# Total Products Ordered: The total number of products in the customer_orders set.
total_products = len(customer_orders)
print("Total product : " + str(total_products))
# Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
sum_product = sum(inventory.values())
print("Sum product " + str( sum_product))
percentage_ordered = (total_products/sum_product)*100
print("Percentage of product ordered : " + str(percentage_ordered))

# 9 Update the inventory by subtracting 1 from the quantity of each product. Modify the inventory dictionary accordingly
for item in customer_orders:
    inventory[item]-=1

# 10 Print the updated inventory, displaying the quantity of each product on separate lines
for item in inventory.items():
    print(item)
