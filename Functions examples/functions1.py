#WAP add 2 numbers use function

#Function definition

def add(x,y):
    c = x+y  #c is a local variable and cannot be accessed outside function
    return c

#Calling a function    

resp = add(50,60)
print(resp)
