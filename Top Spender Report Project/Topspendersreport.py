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
            {"name": "USB-C Hub", "quantity": 1, "price": 50}
        ],
        "status": "delivered"
    }
]

#Function to calculate the total of an order

def total_orderamount(order):
    return sum(item["quantity"] * item["price"] for item in order["items"])

customer_totals = {}

for order in orders:
    customer = order["customer"]
    total_amount = total_orderamount(order)
    if customer not in customer_totals:
        customer_totals[customer] = 0
        customer_totals[customer] += total_amount

print(customer_totals)

#sort customers with highest spent first to lowest
sort_customer = sorted(customer_totals.items(), key=lambda x:x[1], reverse=True)
print(sort_customer)





