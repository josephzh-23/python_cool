from collections import deque

from studyBud.Graph.Util.checkIfGridValid import isInBounds
from studyBud.Graph.bfs_matrix import directions
from studyBud.Graph.print_2d_matrix import printMatrix


# leetcode this problem out

def BFS(grid, vis, row, col):
    # Stores indices of the matrix cells
    q = deque()


    # Mark the starting cell as visited
    # and push it into the queue
    q.append((row, col))
    vis[row][col] = True


    while (len(q) > 0):

        # this allows things to pop from the leftas said
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        
        # Go to the adjacent cells
        for row, col in directions:
            adjx = x + row
            adjy = y + col
            if isInBounds(grid, adjx, adjy) and not vis[adjx][adjy]:
                q.append((adjx, adjy))
                vis[adjx][adjy] = True


# Driver Code
if __name__ == '__main__':
    # Given input matrix
    grid = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]


    row = len(grid)
    col = len(grid[0])
    # print("row and col are " ,row, col)
    vis = [[False for i in range(col)] for i in range(row)]
    # Declare the visited array
    # vis = [[False* col] *row]

    # vis = [[False] * col] * row
    # vis, False, sizeof vis)
    printMatrix(vis)

    BFS(grid, vis, 0, 0)