# review this bad boy, had trouble finding the conditions
# for moving the l/r search boundaries correctly - take time
# to be able to simply explain the intuition for correctly moving 
# the search boundaries

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            m = (r + l) // 2
            #print(l,m,r)
            
            if target == nums[m]:
                return m
            
            if target > nums[m]:
                if target > nums[r] and nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
            else: # target < nums[m]
                if target < nums[l] and nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
                    