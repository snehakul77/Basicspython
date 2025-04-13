#WAP to add to 2 numbers taking inputs from commandline
#check git commit
import sys

def add(x,y):
    return x+y

args= sys.argv[1:]
if len(args) != 2:
    print("invalid args")
    sys.exit(0)

s = add(int(args[0]),int(args[1]))
print(s)
    
