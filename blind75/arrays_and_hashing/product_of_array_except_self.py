class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [1] * len(nums)
        
        # all products w/o self L -> R
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
            
        # products w/o self R -> L
        rollingProduct = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            result[i] *= rollingProduct
            rollingProduct *= nums[i]
            
        return result