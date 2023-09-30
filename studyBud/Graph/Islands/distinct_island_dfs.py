from studyBud.Graph.bfs_matrix import isInBounds

# use a set first
grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]

# output will be 3


class DistinctIslandCounter:
    mySet = set()

    baseRow = 0
    baseCol = 0
    sb = ""

    def __init__(self, graph):
        self.g = graph
    def dfs(s, grid, r, c):
        if not isInBounds(grid, r, c) or grid[r][c] == 0:
            return

        # Change this to 0 first
        grid[r][c] = 0
        # add this to string builder
        s.sb += str(r - s.baseRow)
        s.sb += str(c - s.baseCol)
        print("sb is ", s.sb)

        s.dfs(grid, r - 1, c)
        s.dfs(grid, r + 1, c)
        s.dfs(grid, r, c - 1)
        s.dfs(grid, r, c + 1)

    def distinctIslandCounter(s):
        for r in range(len(s.g)):
            for c in range(len(s.g[0])):
                if (s.g[r][c] == 1):
                    # start traversing here
                
                    s.baseRow = r
                    s.baseCol = c
                    s.sb = ""
                    s.dfs(s.g, r, c)
                    print("I just exited")
                    # add result to unique so we get the unique size here
                    s.mySet.add(s.sb)
        return len(s.mySet)


# the distinct island counter here
s = DistinctIslandCounter(grid)
print(s.distinctIslandCounter())
