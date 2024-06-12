# calculate how many ways to get to finish,
#starting from finish, which equals 1
# remember the restriction - you can only go
# right/down - only need to count r/d sub-solutions

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # finish = 1
        dp[m-1][n-1] = 1

        # pop last row = 1; 
        # cannot move down on bottom row, can only move right - 
        # therefore only 1 route to finish;
        for i in range(n):
            dp[m-1][i] = 1

        # pop last col = 1; same reasoning as bottom row
        # can only move down
        for i in range(m):
            dp[i][n-1] = 1
        
        # iterate backward to start from tile diagonal
        # from bottom right (finish), calculating all 
        # routes as: 
        # routes from current tile to finish = routes from right tile + routes from down tile

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]