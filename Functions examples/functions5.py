#WAF to compute sum and avg of a given list

#we can return multiple values from the function


def get_sum_avg(x):
    total = sum(x)
    avg = total/len(x)
    return total,avg


input_x = [10,20,30,40]

output = get_sum_avg(input_x)
#print(output)      #Returns a tuple of values from function
print("output : {}".format(output))
