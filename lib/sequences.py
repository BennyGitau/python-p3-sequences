#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    
    result = [0] * length  
    if length > 0:
        result[0] = 0 
    if length > 1:
        result[1] = 1  
    for i in range(2, length):
        result[i] = result[i - 1] + result[i - 2]

    print(result)



    

#five factorial
def five_factorial(x):
    result = 1
    for n in range(1, x+1):
        result *= n
    print(result)
    return result

five_factorial(5)
