#Default args : two params

def add(x,y,z=0):
    print("The default z value: {}".format(z))
    return x+y+z

print(f"calling add function with two args: {add(10,20)}")
