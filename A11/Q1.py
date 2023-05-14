# 11127137, 黃乙家

def printPath(path):
    People = ("man", "cabbage", "goat", "wolf")
    boat = 0
    for i in range(1, len(path)):
        passengers = []
        for j in range(len(path[i])):
            if path[i][j] != path[i-1][j]:
                passengers.append(People[j])
        print(i,  end = ". ")
        print("The ",passengers[0], " takes " , "the " + passengers[1] if len(passengers)>1 else "only himself", " from the ", "east " if boat == 0 else "west ", "to the ", "west" if boat == 0 else "east", sep="", end = ".\n" )
        boat ^= 1

print("A solution to the MCGW problem is:")
solution = ["EEEE", "WEWE", "EEWE", "WEWW", "EEEW", "WWEW", "EWEW", "WWWW"]
printPath(solution)

