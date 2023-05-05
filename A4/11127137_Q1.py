#11127137,黃乙家
def merge(list1,list2):
    len1 = 0
    for i in list1:
        len1+=1
    len2 = 0
    for i in list2:
        len2+=1
    ret_list = []
    """
    for i in list1:
        ret_list.append(i)
    for i in list2:
        ret_list.append(i)
    ret_list.sort()
    return ret_list
    """
    it1 = 0
    it2 = 0
    while( it1 + it2 < len1 + len2 ):
        if (it1 != len1) and ( it2 == len2 or list1[it1] < list2[it2]):
            ret_list.append(list1[it1])
            it1+=1
        else:
            ret_list.append(list2[it2])
            it2+=1
    return ret_list

print("Case 1: L1 = [1,3,5,7,9], L2 = [0,2,4,6,8]")
L1 = [1,3,5,7,9]
L2 = [0,2,4,6,8]
print("Merged lists:", merge(L1,L2))

print("\nCase 2: L1 = [1,2,3,4,5,6], L2 = [7,8,9]")
L1 = [1,2,3,4,5,6]
L2 = [7,8,9]
print("Merged lists:", merge(L1,L2))

print("\nCase 3: L1 = [], L2 = [1,2,3,4,5,6,7,8,9]")
L1 = []
L2 = [1,2,3,4,5,6,7,8,9]
print("Merged lists:", merge(L1,L2))

print("\nCase 4: L1 = [1,2,3,4,5,6,7,8,9], L2 = [1,2,3,4,5,6,7,8,9]")
L1 = [1,2,3,4,5,6,7,8,9]
L2 = [1,2,3,4,5,6,7,8,9]
print("Merged lists:", merge(L1,L2))
