from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1] * (amount+1) #from 0 -> amount
        cache[0] = 0

        for a in range(1, len(cache)):
            for c in coins:
                if c > amount:
                    continue
                cache[a] = min(cache[a], cache[a-c] + 1)
        return cache[amount] if cache[amount] != amount+1 else -1

    #TLE (*not even sure this is correct)
    # TLE obviously duplicate subtrees, and solution is 
    # obviously cache results of subtrees on first traversal
    # *having difficulty implemting subtree cache? ...
    def coinChange2(self, coins: List[int], amount: int) -> int:
        minCoins = float('inf')

        for i in range(len(coins)):
            used = self.getCoins(coins,amount,i,0)
            minCoins = min(minCoins, used) 
        return minCoins if minCoins != float('inf') else -1

    def getCoins(self, coins, amount, i, used):
        if amount == 0:
            return used
        if amount - coins[i] < 0 and i == 0:
            return float('inf')

        if amount - coins[i] < 0 and i > 0:
            return self.getCoins(coins, amount, i-1, used)
        if amount - coins[i] > 0 and i == 0:
            return self.getCoins(coins, amount-coins[i], i, used+1)
        return min(self.getCoins(coins, amount-coins[i], i, used+1), self.getCoins(coins, amount-coins[i], i-1, used+1))
            