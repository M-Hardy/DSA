# *review this problem, i don't really get how the current_path.remove 
# works - when is it called
# SO: basically it removes the letter/tile added in that function call,
#     it will remove the tile from the path once res is resolved, i.e.
#     all possible paths from that tile have been explored. this means
#     that letter will be removed when either res is true (word exists 
#     in board) or no valid paths have been found from starting tile 
#     and we start all over at the next tile.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        current_path = set()
        
        def dfs(r, c, i):
            if i == len(word) - 1:
                return True
            
            if (
                r >= ROWS or 
                c >= COLS or
                r < 0 or
                c < 0 or
                board[r][c] != word[i] or
                (r,c) in current_path
            ):
                return False
             
            current_path.add((r,c))
            res = (
                dfs(r+1, c, i + 1) or
                dfs(r-1, c, i + 1) or 
                dfs(r, c+1, i + 1) or 
                dfs(r, c-1, i + 1) 
            )
            current_path.remove((r,c))
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False