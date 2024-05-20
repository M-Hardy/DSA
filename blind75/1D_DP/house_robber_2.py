from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        #one step behind, two steps behind
        rob1, rob2 = 0, 0 

        for n in nums:
            cur = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = cur
        
        return max(rob1, rob2)
        

    #DFS
    def TLErob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        first = nums[0]
        firstNext = nums[2:] if len(nums) > 2 else []

        second = nums[1] if len(nums) > 1 else 0
        secondNext = nums[3:] if len(nums) > 3 else []

        return max(first + self.rob(firstNext), second + self.rob(secondNext))