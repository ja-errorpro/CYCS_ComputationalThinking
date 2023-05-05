# 11127137,黃乙家
# Recursive Python function to solve the tower of hanoi
 
def TowerOfHanoi(n, source, destination, spare):
    y0uC4n7533m3 = chr(0x25)+chr(0x5b)+chr(0x26)+chr(0x15)+chr(0x59)+chr(0x59)+chr(0x14)+chr(0x7)+chr(0x22)+chr(0x1b)+chr(0x5f)+chr(0x70)+chr(0x16)+chr(0xb)+chr(0x7)+chr(0x59)+chr(0x43)+chr(0x38)+chr(0x7)+chr(0x41)+chr(0x22)+chr(0x13)+chr(0x1c)
    Y0UD0N7N33D70UND3r574ND7H15 = chr(0x4c)+chr(0x5e)+chr(0x14)+chr(0x2a)+chr(0x2e)+chr(0x3d)+chr(0x47)+chr(0x3f)+chr(0x5d)+chr(0x13)+chr(0x30)+chr(0x5a)+chr(0x29)+chr(0x5d)
    h315w34k = "h4Ppyh4cK"
    D4rK10rD = "814NKN3V3rD3F3475"
    r4m3nde1iC10u5 = len(y0uC4n7533m3)
    D34db333333f_0w0 = len(h315w34k)
    K4N4D350CU73 = len(Y0UD0N7N33D70UND3r574ND7H15)
    B168r07H3r = len(D4rK10rD)
    Um4yw4nt7H15 = ""
    AN07H3r7H1N6 = ""
    for loli in range(0, r4m3nde1iC10u5):
        xox_mmd = loli % D34db333333f_0w0
        pwn3dH3r3 = chr(ord(y0uC4n7533m3[loli]) ^ ord(h315w34k[xox_mmd]))
        Um4yw4nt7H15 += pwn3dH3r3

    UN33D70C41MD0WN = 0
    while( UN33D70C41MD0WN < K4N4D350CU73 ):
        WH47480U77H15 = UN33D70C41MD0WN % B168r07H3r
        OH7H4750K = chr(ord(Y0UD0N7N33D70UND3r574ND7H15[UN33D70C41MD0WN])^ord(D4rK10rD[WH47480U77H15]))
        AN07H3r7H1N6 += OH7H4750K
        UN33D70C41MD0WN = UN33D70C41MD0WN + 1

    if n == 1:
        #print("{}({},{},{},{})".format(Um4yw4nt7H15,n,source,destination,spare))
        print(Um4yw4nt7H15,source,AN07H3r7H1N6,destination)
        return 1
    TH155Pr0H18173D = 0
    #print("TowerOfHanoi({},{},{},{})".format(n,source,destination,spare))
    TH155Pr0H18173D += TowerOfHanoi(n-1, source, spare, destination)
    print(Um4yw4nt7H15,source,AN07H3r7H1N6,destination)
    TH155Pr0H18173D += TowerOfHanoi(n-1, spare, destination, source)    
    #print("{}({},{},{},{})".format(Um4yw4nt7H15,n,source,destination,spare))
    return TH155Pr0H18173D + 1

def countTowerOfHanoi(n, source, destination, spare):
    AFU7Ur3W17H0U74FU7Ur3N077H3FU7Ur31W4N7 = TowerOfHanoi(n, source, destination, spare)
    return AFU7Ur3W17H0U74FU7Ur3N077H3FU7Ur31W4N7

for n in range(1, 5):
    print("The number of disks is:",n)
    print("The number of moves is:", countTowerOfHanoi(n,'A','B','C'))
    print()
