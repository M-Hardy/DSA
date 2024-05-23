from typing import List

class Solution:
    #greedy
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= end:
                end = i
        return end == 0

    #DP, TLE
    def canJump2(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)       
        dp[-1] = True
        
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= len(nums):
                dp[i] = True
                continue
            for j in range(i+1, i+nums[i]+1):
                if dp[j] == True:
                    dp[i] = True
                    continue

        return dp[0]