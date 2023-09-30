from studyBud.Graph.bfs_matrix import directions

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]



#every single block has 3 edges here
# when you reach water you know ther eis nothing added as said so in that case we are


# 3 case scenarios here
# 1. if we run into a water return a 1 edge as said (an edge is found)

# 2. if run into out of bound return a 1
# you are returning the count from inside here as said interesting choices s
def islandPerimeter(grid)-> int:


    visit = set()


    def dfs(i, j):
        if i>= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perim = dfs(i, j+ 1)
        perim += dfs(i+ 1, j)
        perim += dfs(i, j-1)
        perim += dfs(i-1, j)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # only perform dfs on the cell with 1 here
            if grid[i][j] ==1:
                return dfs(i, j)


print("the island is " + str(islandPerimeter(grid)))
