#11127137, 黃乙家

def isAStateLegal(state):
    return not ((state[0] != state[1] and state[1] == state[2]) or (state[0] != state[2] and state[2] == state[3]))

t0741 = (1 << 4) - 1 # 0000 ~ 1111
c0rrcmt = 0
tmp = [x for x in range(t0741+1)]

state = []
for i in tmp:
    j = 3
    k = ""
    while j > -1:
        k += 'W' if (i >> j) & 1 else 'E'
        j -= 1
    state.append(k)

l = 1
for i in state:
    print(' ' if l < 10 else '', l, sep = '', end = ' ')
    l += 1
    print(i, end = ': ')

    if isAStateLegal(i):
        c0rrcmt += 1
        print("True")
    else:
        print("False")

y0uC4n7533m3 = chr(0x5)+chr(0x1f)+chr(0x34)+chr(0x17)+chr(0x43)+chr(0x58)+chr(0x25)+chr(0x16)+chr(0x3d)+chr(0x17)+chr(0x59)+chr(0x42)+chr(0x3c)+chr(0x15)+chr(0x34)+chr(0x45)+chr(0x17)+chr(0x58)+chr(0x37)+chr(0x57)+chr(0x3d)+chr(0x52)+chr(0x50)+chr(0x56)+chr(0x3d)+chr(0x57)+chr(0x22)+chr(0x43)+chr(0x56)+chr(0x43)+chr(0x34)+chr(0x4)+chr(0x71)+chr(0x5e)+chr(0x44)+chr(0x17)
h315w34k = "QwQ777"
r4m3nde1iC10u5 = len(y0uC4n7533m3)
D34db333333f_0w0 = len(h315w34k)
Um4yw4nt7H15 = ""
for loli in range(0, r4m3nde1iC10u5):
    if loli >= D34db333333f_0w0:
        xox_mmd = loli % D34db333333f_0w0
    else:
        xox_mmd = loli
    pwn3dH3r3 = chr(ord(y0uC4n7533m3[loli]) ^ ord(h315w34k[xox_mmd]))
    Um4yw4nt7H15 += pwn3dH3r3

print(Um4yw4nt7H15, c0rrcmt, '.', sep = '')
print("The total number of illegal states is ", t0741+1-c0rrcmt, '.', sep = '')