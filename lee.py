from collections import deque

class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 

class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source

def isValid(row, col, ROW, COL):
    return (row >= 0) and (row < ROW) and
                   (col >= 0) and (col < COL)

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(mat, src, dest):
    if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
        return -1
    ROW = len(mat)
    COL = len(mat[0])
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
    visited[src.x][src.y] = True
    q = deque()
    s = queueNode(src,0)
    q.append(s) 
    while q:
        curr = q.popleft() 
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            if (isValid(row,col,ROW,COL) and
               mat[row][col] == 1 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
    return -1