# *review problem, implement dfs solution for practice

import collections
from typing import List

class Solution:
    # only check perimeter (touch an ocean by default)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def bfs(row,col,visited):
            q = collections.deque()
            q.append((row,col,heights[row][col])) 
            
            while q:
                r, c, prev = q.popleft()
                if (
                    r >= ROWS or
                    r < 0 or
                    c >= COLS or
                    c < 0 or
                    heights[r][c] < prev or 
                    (r,c) in visited
                ):
                    continue
                visited.add((r,c))
                prev = heights[r][c]
                q.append((r+1,c,prev))
                q.append((r-1,c,prev))
                q.append((r,c+1,prev))
                q.append((r,c-1,prev))
            
        # get all tiles that can touch pacific starting from
        # pacific perimeter
        for c in range(COLS):
            bfs(0, c, pac)
            bfs(ROWS-1, c, atl)
            
        # get all tiles that can touch atlantic starting from
        # atlantic perimeter
        for r in range(ROWS):
            bfs(r, 0, pac)
            bfs(r, COLS-1, atl)
        
        res = []
        for tile in pac:
            if tile in atl:
                r,c = tile
                res.append([r,c])
                
        return res
        
        
    # brute force bfs, TLEs at 111/113
    def TLEpacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        connected = [] 
        
        def bfs(r,c):
            start = [r,c]
            q = collections.deque()
            q.append((r,c))
            
            path = set()
            atlantic = False
            pacific = False
            
            while q:
                row, col = q.popleft()
                path.add((row,col))
                
                if row == 0 or col == 0:
                    pacific = True
                if row == ROWS-1 or col == COLS-1:
                    atlantic = True
                if (pacific and atlantic): 
                    connected.append(start)
                    return
                
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for rd, cd in directions:
                    r,c = row+rd, col+cd
                    if (
                        -1 < r < ROWS and
                        -1 < c < COLS and
                        heights[r][c] <= heights[row][col] and
                        (r,c) not in path
                    ):
                        q.append([r,c])
        
        
        for r in range(ROWS):
            for c in range(COLS):
                bfs(r,c)
        return connected