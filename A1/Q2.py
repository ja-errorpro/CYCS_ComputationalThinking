# Author: YiJia, 11127137

def main():
    n = eval(input("Enter an odd integer for this game >> "))
    x = eval(input("Your turn: enter an uncalled integer between 0 and " + str(n) + " inclusive >>"))
    while x >= 0:
        print("Computer's turn: ", end = " ")
        print(n - x)
        x = eval(input("Your turn: enter an uncalled integer between 0 and " + str(n) + " inclusive >>"))
        print("Thank you for using the program.")

main()