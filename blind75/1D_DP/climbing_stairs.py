class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        oneStep = 1
        twoSteps = 2
        for s in range(3, n):
            cur = oneStep + twoSteps
            oneStep = twoSteps
            twoSteps = cur

        return oneStep + twoSteps

    def ARRAYclimbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        stairs = [0] * (n+1)
        for i in range(3):
            stairs[i] = i

        for s in range(3, n+1):
            stairs[s] = stairs[s-1] + stairs[s-2]

        return stairs[-1]

    #DFS
    def TLEclimbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)