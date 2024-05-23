# note - there is also a binary search solution

from typing import List

class Solution:
    #dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)


    # Still TLEs despite alternate memoization
    # caching still not reducing decision tree substantially enough
    def STILL_TLES_2_lengthOfLIS(self, nums: List[int]) -> int:
        cache = {} #(last two indices of subseq): length of LIS
        return self.helper(nums, 0, -1, cache)

    def helper(self, nums, index, last_index, cache):
        if index >= len(nums):
            return 0
        if index in cache:
            return cache[index]
        
        skip = self.helper(nums, index+1, last_index, cache)
        take = 0
        if last_index == -1 or nums[index] > nums[last_index]:
            take = 1 + self.helper(nums, index+1, index, cache)
            
        if index not in cache:
            cache[index] = max(skip, take)
        else:
            cache[index] = max(skip, take, cache[index])
        return cache[index]


    # Still TLEs despite memoization 
    # caching is not reducing decision tree substantially enough
    def STILL_TLE_lengthOfLIS(self, nums: List[int]) -> int:
        cache = {} #idx:longest subseq found at num
        return self.helper2(nums, 0, float('-inf'), cache)

    def helper2(self, nums, i, last, cache):
        if i >= len(nums):
            return 0 
        if (i, last) in cache:
            return cache[(i,last)]

        skip = self.helper2(nums, i+1, last, cache)
        take = 0
        if nums[i] > last:          
            take = 1 + self.helper2(nums,i+1,nums[i],cache) 

        cache[(i,last)] = max(skip, take)
        return cache[(i,last)]

    # no memoization, TLE
    def DFS_TLE_lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper3(nums, 0, [])

    def helper3(self, nums, i, cur):
        if i >= len(nums):
            return len(cur) 
        if cur and nums[i] <= cur[-1]:
            return self.helper3(nums, i+1, cur)
        if not cur or (cur and nums[i] > cur[-1]):
            add = cur[:] #deep copy
            add.append(nums[i])
            return max(self.helper3(nums, i+1, cur), self.helper3(nums, i+1, add))