# 11127137, 黃乙家

def printStates():
    ret = [x for x in range(0b1111 + 1)]
    # 0: E, 1: W
    
    retstrs = []
    for i in ret:
        j = 3
        rs = ""
        while ( j > -1 ):
            if ( i >> j & 1 ):
                rs += "W" 
            else:
                rs += "E"
            j -= 1
        retstrs.append(rs)

    retstrs.sort()
    cnt = 1
    for i in retstrs:
        print( str(cnt) + ": " + i )
        cnt += 1

printStates()
