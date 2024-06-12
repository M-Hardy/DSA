from typing import List

class Solution:
    # key difference with verbose is to always increment cur 
    # with current element. if cur is negative reset to 0 
    # and increment with current element (i.e. 'reset' cur to current 
    # element)
    # therefore - if cur is negative, and next is also negative, it will
    # only be one negative value (will not accumulate); if next is postiive
    # it 'restarts' with positive value
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            res = max(cur, res)
        return res

    #grind 75 test
    def VERBOSEmaxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):
            if cur >= 0:
                cur += nums[i]
                maxSum = max(cur, maxSum)
            
            else:
                maxSum = max(cur, maxSum, nums[i])
                cur = nums[i]

        return maxSum