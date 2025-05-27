orders = [
    {
        "order_id": 1001,
        "customer": "Alice",
        "items": [
            {"name": "Laptop", "quantity": 1, "price": 900},
            {"name": "Mouse", "quantity": 2, "price": 20}
        ],
        "status": "delivered"
    },
    {
        "order_id": 1002,
        "customer": "Bob",
        "items": [
            {"name": "Keyboard", "quantity": 1, "price": 45}
        ],
        "status": "shipped"
    },
    {
        "order_id": 1003,
        "customer": "Charlie",
        "items": [
            {"name": "Monitor", "quantity": 2, "price": 150},
            {"name": "HDMI Cable", "quantity": 3, "price": 10}
        ],
        "status": "pending"
    },
    {
        "order_id": 1004,
        "customer": "Alice",
        "items": [
            {"name": "USB-C Hub", "quantity": 1, "price": 50},
            {"name": "Monitor", "quantity": 1, "price": 150}
        ],
        "status": "delivered"
    }
]

#Find the customer who ordered the most items in total (sum of all quantities, across all orders)

#cust_dict ={}
#for order in orders:
#    quantity = 0
#    for item in order["items"]:
#        quantity += item["quantity"]
#    #print(quantity)
#    name = order["customer"]
#    quantity = quantity
#    if name not in cust_dict:
#        cust_dict[name] = 0
#    cust_dict[name] += quantity
#print(cust_dict)

#max_spent = max(cust_dict.items(), key=lambda x:x[1])
#print(max_spent)

#Loop through all items in all orders and create a dictionary of total quantity ordered for each item.
quantity_dict = {}
for order in orders:
    for item in order["items"]:
        name = item["name"]
        quantity = item["quantity"]
        if name not in quantity_dict:
            quantity_dict[name] = 0
        quantity_dict[name] += quantity
print(quantity_dict)

least_quant = min(quantity_dict.items(), key=lambda x:x[1])
print(least_quant)






