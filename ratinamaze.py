def printPathHelper(x, y, maze, n, solution):

    #Destination Cell
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        print(solution)
        
        return
    # these are the Blocking Points
    if x < 0 or y < 0 or x >=n or y >= n or maze[x][y] == 0 or solution[x][y] == 1:
        return
    solution[x][y] = 1
    #print("solution first wala",solution)
    #down
    printPathHelper(x + 1, y, maze, n, solution)
    
    #right
    printPathHelper(x, y + 1, maze, n, solution)
    
    #top
    printPathHelper(x - 1, y, maze, n, solution)
    
    #left
    printPathHelper(x, y - 1, maze, n, solution)
    solution[x][y] = 0
##    print("solutionnn", solution)
##    print("solution", x, '==',y)
    return

def printPath(maze):
    n = len(maze)
    
    solution = [[0 for j in range(n)]for i in range(n)]
    #print(solution)
    printPathHelper(0, 0, maze, n, solution)


n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
printPath(maze)




