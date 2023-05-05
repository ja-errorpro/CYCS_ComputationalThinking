# Author: 黃乙家,11127137
def conversion(mark):
    print(chr(ord('A')+(mark<=75)+(mark<=60)+(mark<=45)))

conversion(0)
conversion(10)
conversion(60)
conversion(65)
conversion(75)
conversion(100)
