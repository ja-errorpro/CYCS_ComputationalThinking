# 11127137, 黃乙家

def isNeighbor(G, node1, node2):
    try:
        return node2 in G[node1] or node1 in G[node2]
    except KeyError:
        return False

def setNeighbors(G, node):
    _ = set()
    try:
        for __ in G[node]:
            _.add(__)
    except KeyError:
        return None
    return _

def numNodes(G):
    return len(G)

def numLinks(G):
    _ = 0
    for __ in G:
        _ += len(G[__])
    return int(_/2)

aGraph = {"EEEE": {"WEWE"},
"WEWE": {"EEEE", "EEWE"},
"EEWE": {"WEWE", "WEWW", "WWWE"},
"WEWW": {"EEWE", "EEEW"},
"EEEW": {"WEWW", "WWEW"},
"WWWE": {"EEWE", "EWEE"},
"EWEE": {"WWWE", "WWEW"},
"WWEW": {"EEEW", "EWEE", "EWEW"},
"EWEW": {"WWEW", "WWWW"},
"WWWW": {"EWEW"}}

# Testing isNeighbor()
print("Testing isNeighbor():")
for i in aGraph.keys():
    print("For node "+i+":")
    for j in aGraph.keys():
        print("- Neighbor with "+j+": "+str(isNeighbor(aGraph,i,j)))

print("\nTesting setNeighbors():")
# Testing setNeighbors()
for i in aGraph.keys():
    print("Neighbors of node "+i+":", setNeighbors(aGraph, i))

print("\nTesting numNodes():")
# Testing numNodes()
print("The number of nodes in the graph is "+str(numNodes(aGraph))+".")

print("\nTesting numLinks():")
# Testing numLinks()
print("The number of links in the graph is "+str(numLinks(aGraph))+".")
