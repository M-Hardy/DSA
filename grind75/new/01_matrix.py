from typing import List
import collections

class Solution:
    # trick: do BFS from target -> source, not source -> target
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        DIRS = [(1,0), (0,1), (-1, 0), (0,-1)]
        visited = set()
        q = collections.deque()

        #populate res array
        res = [[0] * COLS for _ in range(ROWS)]

        #populate q with 0s from matrix
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        
        # BFS
        while q:
            #for each layer in bfs
            for _ in range(len(q)):
                r,c = q.popleft()

                if mat[r][c] == 1:
                    res[r][c] = dist
                
                for dr,dc in DIRS:
                    nr = r+dr
                    nc = c+dc

                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            dist += 1

        return res



    ### PREVIOUS ATTEMPTS ###

    # caching incorrect - premature return on found may not be
    # shortest path
    """
    def bfs2(self, startR, startC, ROWS, COLS, DIRS, found):
        q = collections.deque()
        q.append((startR,startC))
        visited = set() 

        while q:
            (r, c) = q.popleft()

            if (r,c) in found:
                return abs(r-startR) + abs(c-startC) + found[(r,c)]

            if mat[r][c] == 0:
                found[(startR, startC)] = abs(r-startR) + abs(c-startC)

                for visitedR,visitedC in visited:
                    found[(visitedR, visitedC)] = abs(r-visitedR) + abs(c-visitedC)
                    
                return found[(startR, startC)]

            for dr, dc in DIRS:
                newR, newC = r+dr, c+dc

                if (-1 < newR < ROWS and 
                    -1 < newC < COLS and
                    (newR,newC) not in visited
                ):
                    q.append((newR,newC))

            visited.add((r,c))

        return COLS
    """

    #brute force BFS, TLE
    """
    def bfs3(self, startR, startC):
        q = collections.deque()
        q.append((startR,startC))
        visited = set() 

        while q:
            (r, c) = q.popleft()

            if mat[r][c] == 0:
                return abs(r-startR) + abs(c-startC)

            for dr, dc in DIRS:
                newR, newC = r+dr, c+dc

                if (-1 < newR < ROWS and 
                    -1 < newC < COLS and
                    (newR,newC) not in visited
                ):
                    q.append((newR,newC))

            visited.add((r,c))

        return COLS
    """