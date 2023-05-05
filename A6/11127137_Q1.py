# 11127137,黃乙家
# Recursive Python function to solve the tower of hanoi
 
def TowerOfHanoi(n, source, destination, spare):
    y0uC4n7533m3 = chr(0x37)+chr(0x00)+chr(0x1a)+chr(0x15)+chr(0x1b)+chr(0x23)+chr(0x03)+chr(0x2d)+chr(0x13)+chr(0x1c)+chr(0x5f)+chr(0x1b)
    h315w34k = "compileerr0r"
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

    if n == 1:
        print("{}({},{},{},{})".format(Um4yw4nt7H15,n,source,destination,spare))
        #print("Move 1 disk from source",source,"to destination",destination)
        return 1
    x = 0
    #print("TowerOfHanoi({},{},{},{})".format(n,source,destination,spare))
    x += TowerOfHanoi(n-1, source, spare, destination)
    #print("Move 1 disk from source",source,"to destination",destination)
    x += TowerOfHanoi(n-1, spare, destination, source)    
    print("{}({},{},{},{})".format(Um4yw4nt7H15,n,source,destination,spare))
    return x + 1

for n in range(1, 5):
    print("The number of disks is:",n)
    TowerOfHanoi(n,'A','B','C')
    print()
