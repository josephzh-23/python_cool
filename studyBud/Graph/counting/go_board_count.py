from collections import deque

from studyBud.Graph.Util.checkIfGridValid import isInBounds
from studyBud.Graph.bfs_matrix import directions


# very good stuff this means you are pretty good at this
w = 'w'
b = 'b'
e = 'e'

# place this
goBoard = [['e', 'e', 'e', 'e','b', 'b', 'b'],
           ['e', 'e', 'e', 'b','w', 'w', 'b'],
           ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
           ['e', 'e', 'e', 'e', 'e', 'e', 'e']]



# r and c are the starting poitn here
def checkSurrounded(grid, r, c):
    rowSize = len(grid)
    colSize = len(grid[0])
    vis = [[False for i in range(colSize)] for i in range(rowSize)]

    # Stores indices of the matrix cells
    q = deque()

    count = 0

    # Mark the starting cell as visited
    # and push it into the queue
    q.append([r, c])
    vis[r][c] = True

    while (len(q) > 0):

        # this allows things to pop from the leftas said
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        # Go to the adjacent cells
        for [row, col] in directions:
            adjx = x + row
            adjy = y + col
            if isInBounds(grid, adjx, adjy) and not vis[adjx][adjy]:
                if grid[adjx][adjy] == 'w':
                    q.append([adjx, adjy])
                    count+=1
                    vis[adjx][adjy] = True

        print("the count is ", count)

checkSurrounded(goBoard, 2, 5)
