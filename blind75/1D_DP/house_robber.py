from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # don't need these variables, only using it once
        # (not reusing multiple times); can enter the slices
        # directly in function call to be more concise
        rob1 = nums[:-1]
        rob2 = nums[1:]
        
        return max(self.robHelper(rob1), self.robHelper(rob2))

    def robHelper(self, nums):
        #one step behind, two steps behind
        rob1, rob2 = 0, 0   

        for n in nums:
            cur = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = cur
        
        return max(rob1, rob2)