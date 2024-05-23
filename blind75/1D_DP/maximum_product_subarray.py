# trick is to keep track of current max AND current min
# the idea is that they basically swap each time a negative
# value is encountered so you have the correct current max
# at each negative value
# also worth noting that we are also comparing cur value with
# cur max and cur min - this lets us 'restart' cur max/cur min 
# if a neg/pos value is encountered, or a 0 is encountered for 
# either

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = float('-inf')
        curMax, curMin = 1,1

        for n in nums:
            tmp = curMax 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            maxProd = max(maxProd, curMax)

        return maxProd