

# this makes sure no array out of bound exce

def isInBoundInt(vis, x, y):
    if x < 0 or y < 0 or x >=len(vis) or y >= len(vis[0]):
        return False

    if vis[x][y]:
        return False

    #otherwise
    return True
