#11127137,黃乙家

def countChar():
    inputstr = input("Please enter a word consisting of only English alphabets in lower cases: ")
    alphabets = [chr(ord('a')+x) for x in range(26)]
    freq = []
    for i in alphabets:
        freq.append(inputstr.count(i))
    
    for i in range(26):
        print( "# of {} : {}".format(alphabets[i],freq[i]))

countChar()
