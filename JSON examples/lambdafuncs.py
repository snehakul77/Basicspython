#map and filter with lambda functions

x = [2,4,6,8]
s = list(map(lambda e : e*e,x))
print("map",s)

y = range(1,20)
s2 = list(filter(lambda e: e % 2 == 0,y))
print("filter output" ,s2)
