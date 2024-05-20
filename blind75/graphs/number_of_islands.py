# implementation detail: be careful with initializing
# r,c in the nested for-loop, initially kept it as
# row,col and it will fail test cases as it will update
# the row,col variables outside the for-loop

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        islands = 0
        visited = set()
        
        def bfs(r, c):
            
            q = deque()
            q.append((r,c)) 
            visited.add((r,c))
            
            while q:
                (row, col) = q.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                
                for rd, cd in directions:
                    r, c = row+rd, col+cd
                    
                    if (-1 < r < ROWS and 
                        -1 < c < COLS and 
                        (r,c) not in visited and 
                        grid[r][c] == "1"
                    ):
                        q.append((r, c))
                        visited.add((r, c))
        
        for c in range(COLS):
            for r in range(ROWS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands     