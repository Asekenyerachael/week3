def fizzbuzz(a, b):

    if type(a) is not list or type(b) is not list:
        return "Invalid input"

    sum = len(a)+len(b)

    if sum%5 is 0 and sum%3 is 0:
        return "fizzbuzz"  
    elif sum%3 is 0:
        return "fizz"
    elif sum%5 is 0:
        return "buzz"  
    else:
        return sum
    
print(fizzbuzz([12,2,4,5,8,5,7],[2,3,4,6,9,54,3]))