# Author: YiJia, 11127137

def add2n(n):
    x = 1 / n
    sum = 0
    for i in range(2*n):
        sum += x
    return sum

inaccur = []

for i in range(1,10):
    x = add2n(i)
    print(str(i) + ': ' + str(x))
    if x != 2:
        inaccur.append(i)

print('The following numbers do not give a value of 2:', end = ' ')
[print(i, end = ' ') for i in inaccur]