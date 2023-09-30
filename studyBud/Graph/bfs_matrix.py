from collections import deque as queue

from print_list import printList
from studyBud.Graph.Util.checkIfGridValid import isInBounds
from studyBud.Graph.print_2d_matrix import printMatrix

# Direction vectors


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]



# Function to check if a cell
# is be visited or not



# Function to perform the BFS traversal
def BFS(grid, row, col):
    vis = [[False for i in range(len(grid[0]))] for i in range(len(grid))]

    # Stores indices of the matrix cells
    q = queue()


    # Mark the starting cell as visited
    # and push it into the queue
    q.append([row, col])
    vis[row][col] = True


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
                q.append([adjx, adjy])
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
    # Declare the visited array
    # vis = [[False* col] *row]

    # vis = [[False] * col] * row
    # vis, False, sizeof vis)
    # printMatrix(vis)

    BFS(grid,0, 0)