class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        found = {}
        
        for i, num in enumerate(nums):
            if target - num in found:
                return [i, found[target-num]]
            found[num] = i