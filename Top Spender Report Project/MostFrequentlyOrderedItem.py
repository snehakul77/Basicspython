item_totals = {
    "Laptop": 1,
    "Mouse": 2,
    "Monitor": 2,
    "HDMI Cable": 3,
}

# find out which item was ordered the most across all orders, based on total quantity, regardless of customer.

most_ordered = max(item_totals.items(), key=lambda x:x[1])
print(f" Most ordered item is {most_ordered[0]} and quantity is {most_ordered[1]}")