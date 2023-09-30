from studyBud.Graph.Util.checkIfGridValid import ifValidGrid

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]

# dfs number of islands problem leet
# the above is the grid here and then what do we do here ?
# and then the frist thing

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# how to deal with this as said?


def numIslands(grid):

    numIslands = 0

    # check number of islands here
    if not grid or len(grid) == 0:
        return numIslands

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] == "1":
                numIslands += 1
                callDfs(grid, row, col)
    return numIslands


def callDfs(grid, row, col):
    if not ifValidGrid(grid, row, col):
        return

    if grid[row][col] == "0":
        return

    # mark sth as visited here
    grid[row][col] = "0"

    # expand the search in all directions here
    for rowInc, colInc in directions:
        callDfs(grid, row + rowInc, col + colInc)



print(numIslands(grid))









