class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # is not rotated 
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
                
            else: # if nums[m] < nums[r], cannot be == because all elements are unique
                r = m
                
        return nums[l]     