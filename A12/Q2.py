# 11127137, 黃乙家 

def findShortestPathPlusCalls(graph, start, end, path=[]):
    path = path + [start]
    c = 1
    if start == end:
        return path, c
    if not (start in graph):
        return None, c
    shortestPath = None
    for node in graph[start]:
        if node not in path:                                
            newpath, d = findShortestPathPlusCalls(graph, node, end, path)
            c += d
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath

    return shortestPath, c

def findShortestPath(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    if not (start in graph): 
        return None 
    shortestPath = None 
    for node in graph[start]: 
        if node not in path: 
            newpath = findShortestPath(graph, node, end, path) 
            if newpath: 
                if not shortestPath or len(newpath) < len(shortestPath): 
                    shortestPath = newpath 
                
    return shortestPath

G ={"EEEE": ["WEWE"], "EEEW": ["WEWW", "WWEW"], "EEWE": ["WEWE", "WWWE", "WEWW"],
    "EWEE": ["WWEW", "WWWE"], "EWEW": ["WWEW", "WWWW"], "WEWE": ["EEEE", "EEWE"], 
    "WEWW": ["EEEW", "EEWE"], "WWEW": ["EWEE", "EWEW", "EEEW"], "WWWE": ["EEWE", "EWEE"],
    "WWWW": ["EWEW"]} 

path, totalCall = findShortestPathPlusCalls(G,"EEEE","WWWW") 
print("The shortest path: ", path) 
print("The total number of recursive function calls is:", totalCall)
