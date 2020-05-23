pathRow = [2, 1, -1, -2, -2, -1, 1, 2]
pathCol = [1, 2, 2, 1, -1, -2, -2, -1]

def knightTour(visited, row, col, move):
    if(move == 64):
        for i in range(0, 8):
            for j in range(0, 8):
                print(visited[i][j], end = " ")
            print()

        return True
    else:
        for i in range(len(pathRow)):
            rowNew = row + pathRow[i]
            colNew = col + pathCol[i]
            if(ValidMove(visited, rowNew, colNew)):
                move += 1
                visited[rowNew][colNew] = move
                if(knightTour(visited, rowNew, colNew, move)):
                    return True
                move -= 1
                visited[rowNew][colNew] = 0
    return False


def ValidMove(visited, rowNew, colNew):
    if((rowNew >= 0)and(rowNew < 8)and (colNew >= 0) and (colNew < 8) and (visited[rowNew][colNew] == 0)):
        return True
    return False
from sys import setrecursionlimit
setrecursionlimit(10000)
visited = [[0 for i in range(8)] for j in range(8)]
#print(visited)
visited[0][0] = 1
knightTour(visited, 0, 0, 1)
    
        
             
    
