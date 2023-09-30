from collections import deque

from studyBud.Graph.Util.checkIfGridValid import isInBounds
from studyBud.Graph.bfs_matrix import directions
from studyBud.Graph.print_2d_matrix import printMatrix


grid = [['X','X','X','X','X','X'],
        ['X','*','O','O','O','X'],['X','O','O','#','O','X'],
        ['X','X','X','X','X','X']]
# leetcode this problem out

# keep track of the step here please!!
def shortestPathToGetFood(grid):
    # Stores indices of the matrix cells
    q = deque()
    visited = set()

    rows, cols = len(grid), len(grid[0])
    # step1: For all strating point add the
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == '*'):
                q.append([row, col, 0])
                visited.add((row, col))
                break
    while q:
        x, y, step = q.popleft()


        #check for the return here
        if grid[x][y] == '#':
            return step

        print(grid[x][y], end=" ")
        for row, col in directions:
            adjx = x + row
            adjy = y + col
            if isInBounds(grid, adjx, adjy) and (adjx, adjy) not in visited and \
                grid[adjx][adjy] != 'X':
                q.append([adjx, adjy, step+1])
                visited.add((adjx, adjy))


# Driver Code
if __name__ == '__main__':
    # Given input matrix
    print(shortestPathToGetFood(grid))