# 11127137, 黃乙家

def countChar():
    _ = input("Please enter a word consisting of only English alphabets in lower cases:\n")
    __ = {chr(___): 0 for ___ in range(ord('a'), ord('z')+1)}
    for ___ in _:
        __[___] += 1
    for ___ in __:
        print( "# of", ___, ":", __[___] )

countChar()
