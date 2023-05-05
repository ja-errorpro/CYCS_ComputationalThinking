# 11127137, 黃乙家
def isNeighbor(G, node1, node2 ):
    return 1 if G[node1][node2] == 1 or G[node2][node1] == 1 else 0

def setNeighbors(G, node):
    _ = set()
    for __ in range(len(G)):
        if G[node][__] == 1:
            _.add(__)

    return _

def numNodes(G):
    return len(G)

def numLinks(G):
    _ = 0
    for __ in G:
        for ___ in __:
            if ___ == 1:
                _ += 1
    return int(_/2)

aGraph = [[0,1,0,0,0,0,0,0,0,0], \
[1,0,1,0,0,0,0,0,0,0], \
[0,1,0,1,0,1,0,0,0,0], \
[0,0,1,0,1,0,0,0,0,0], \
[0,0,0,1,0,0,0,1,0,0], \
[0,0,1,0,0,0,1,0,0,0], \
[0,0,0,0,0,1,0,1,0,0], \
[0,0,0,0,1,0,1,0,1,0], \
[0,0,0,0,0,0,0,1,0,1], \
[0,0,0,0,0,0,0,0,1,0]]
# Testing isNeighbor()
print("Testing isNeighbor():")
for i in range(len(aGraph)):
    for j in range(len(aGraph)):
        if isNeighbor(aGraph, i, j):
            print("1", end = "")
        else:
            print("0", end = "")
    print()

print("\nTesting setNeighbors():")
# Testing setNeighbors()
for i in range(len(aGraph)):
    print("Neighbors of node "+str(i)+":", setNeighbors(aGraph, i))

print("\nTesting numNodes():")
# Testing numNodes()
print("The number of nodes in the graph is "+str(numNodes(aGraph))+".")
print("\nTesting numLinks():")
# Testing numLinks()
print("The number of links in the graph is "+str(numLinks(aGraph))+".")
