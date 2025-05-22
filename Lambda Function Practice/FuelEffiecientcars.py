cars = [
    {"make": "Toyota", "model": "Camry", "mpg": 29},
    {"make": "Honda", "model": "Civic", "mpg": 32},
    {"make": "Ford", "model": "F-150", "mpg": 20},
    {"make": "Tesla", "model": "Model 3", "mpg": 130},  # Equivalent MPG for electric
    {"make": "Chevrolet", "model": "Malibu", "mpg": 27}
]

mostefficient = max(cars, key= lambda car: car["mpg"])
leastefficient = min(cars, key= lambda car: car["mpg"])



print(f"Most Efficient Car is: {mostefficient["make"]} {mostefficient["model"]} ({mostefficient["mpg"]}MPG)")
print(f"Least Efficient Car is: {leastefficient["make"]} {leastefficient['model']} ({leastefficient['mpg']}MPG)")
