def ifValidGrid(grid, r, c):
    nr = len(grid)
    nc = len(grid[0])
    if 0 <= r < nr and 0 <= c < nc:
        return True
    else:
        return False


def isInBounds(graph, row, col):
    # If cell lies out of bounds
    if row < 0 or col < 0 or row >= len(graph) or col >= len(graph[0]):
        return False

    # Otherwise
    return True