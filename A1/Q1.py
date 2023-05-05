# Author: YiJia, 11127137

def sum(x, y):
    result = 0
    nextNumber = x
    while nextNumber <= y:
        result = result + nextNumber
        nextNumber = nextNumber + 1
    return result


# Testing Code
print("x = 1 and y = 10:",end = " ")
print(sum(1, 10))
print("x = 5 and y = 10:",end = " ")
print(sum(5, 10))
print("x = -5 and y = 5:",end = " ")
print(sum(-5, 5))