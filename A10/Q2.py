# 11127137, 黃乙家

def genGraph(S):
    S = genLegalStates(S)
    graph = {}
    for i in S:
        graph[i] = set()
        for j in S:
            if isNeighborNode(i, j):
                graph[i].add(j)
    return graph

def genLegalStates(S):
    ret = []
    for i in S:
        if isAStateLegal(i):
            ret.append(i)
    return tuple(ret)

def isAStateLegal(state):
  if state[0] != state[1] and state[1] == state[2]:
      return False
  if state[0] != state[2] and state[2] == state[3]:
      return False
  return True

def isNeighborNode(n1, n2):
    if n1[0] == n2[0]:
        return False
    cnt = 0
    for i in range(1, len(n1)):
        if n1[i] != n2[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True


allStates = ('EEEE', 'EEEW', 'EEWE', 'EEWW', 'EWEE', 'EWEW', 'EWWE', 'EWWW', \
'WEEE', 'WEEW', 'WEWE', 'WEWW', 'WWEE', 'WWEW', 'WWWE', 'WWWW')

G = genGraph(allStates)
for i in G:
    print("’"+i+"’:",G[i])
