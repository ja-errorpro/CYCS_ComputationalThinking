# Author: YiJia, 11127137

def testNumber(number):
    sum = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            sum += i
    return sum == number

for x in [6, 28, 75, 2022]:
    if testNumber(x):
        print(x, "is a p-number.")
    else:
        print(x, "is not a p-number.")