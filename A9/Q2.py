# 11127137, 黃乙家

def isAStateLegal(state):
    # Boat, Man, Ape, Bull, Rhino, Goat, Cabbage
    if state[0] != state[1] and state[0] != state[2]:
        return False
    if state[1] != state[2] and state[2] == state[3]:
        return False
    if state[1] != state[2] and state[2] == state[5]:
        return False
    if state[1] != state[3] and state[3] == state[4]:
        return False
    if state[1] != state[5] and state[5] == state[6]:
        return False
    return True

o = 1 << 7
oo = []
ooo = []

for _ in range(o):
    ____ = ""
    for __ in range(7):
        ___ = (_ >> __) & 1
        if ___ == 0:
            ____ += "E"
        else:
            ____ += "W"
    ____ = ____[::-1]
    if isAStateLegal(____):
        oo.append(____)
    else:
        ooo.append(____)

print("There are " + str(len(oo)) + " legal states:" )
print()
__ = 0
for _ in oo:
    print( _, end = '')
    print( ' ' if __ < 4 else '\n', end = '' )
    __ = ( __ + 1 ) % 5
print()

print()
print("There are " + str(len(ooo)) + " illegal states:" )
print()
__ = 0
for _ in ooo:
    print( _, end = '')
    print( ' ' if __ < 4 else '\n', end = '' )
    __ = ( __ + 1 ) % 5
print()
