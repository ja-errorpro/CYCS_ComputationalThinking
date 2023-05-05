# Author: 黃乙家, 11127137
def count_char(input_string, char):
    return input_string.count(char)

def main():
    s = input('Please enter a string: ')
    c = input('Please enter a character: ')
    print("The number of '{}' in the input string '{}' is {}.".format( c, s, count_char(s,c)))

main()
