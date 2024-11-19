#Inventory data asked tuples (item_name,quantity,price)
inventory=[
    ("laptop",5,30000),
    ("headphones",15,500),
    ("mouse",50,150),
    ("keyboard",20,150),
    ("monitor",10,3000)

]
highest_value=0
for item in inventory:
    item_name,quantity,unit_price=item
    total_price=quantity*unit_price
    print("item_name is",{item_name},"the total price is",{total_price})
    if total_price>highest_value:
        highest_value=total_price
        item_with_highest_value=item_name
print("highest value is ",highest_value)
print("The item with highest stock value is ",item_with_highest_value)





