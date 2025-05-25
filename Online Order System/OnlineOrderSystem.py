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
    }
]


#Calculate total amount for each order (sum of quantity × price for all items)
# Find the customer who spent the most - written by sneha
###for order in orders:
#    Order_total = 0
#    for item in order["items"]:
#        total_price = item["quantity"] * item["price"]
 #       Order_total += total_price
#    print(f" Order Total for order id {order['order_id']}: {Order_total}")
#max_spent = max(orders , key=lambda items: item["quantity"] * item["price"])
#print(f" Order with max spent: {max_spent['order_id']}"

###### Fixed version###

def calculate_order_total(order):
    return sum(item["quantity"] * item["price"] for item in order["items"])

#max_order = max(orders, key=calculate_order_total)
sort_order =sorted(orders, key=calculate_order_total, reverse=True)
for item in sort_order:
    print(item["order_id"])
#List all orders that are "pending"

for order in orders:
    if order["status"] == "pending":
        print(f" Order Status for order {order['order_id']}: {order['status']}")

#Group orders by status

orders_status = {}
for order in orders:
    status = order["status"]
    orderdetails = order
    if status not in orders_status:
        orders_status[status] = []
    orders_status[status].append(orderdetails)

for status, orders in orders_status.items():
    print(f"status: {status}")
    for order in orders:
        print(f"order: {order['order_id']}, Customer: {order['customer']}")






