# (1) if left-most value is positive, all other numbers will
#     be positive because nums is sorted, so no other combinations
#     will sum to 0 from this point on - we can therefore short-circuit
# (2) avoid duplicates by incrementing l & m pointers if previous num 
#     was the same num; note that m pointer increment happens at the end
#     of the loop so that the m < r check applies first before the new
#     m value is used (if you do it within the while-body, m can equal r 
#     and you use an invalid triplet)
# note: there is probably a way to use binary search instead of two-pointer
#       which may be faster

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        result = []
           
        for l in range(len(nums)):
            if nums[l] > 0: # (1)
                break
                
            if l != 0 and nums[l] == nums[l-1]: # (2)
                continue
                
            r = len(nums) - 1
            m = l + 1
            
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                
                if total > 0:
                    r -= 1
                    
                elif total < 0:
                    m += 1
                    
                else: #elif total == 0:
                    result.append([nums[l],nums[m],nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m-1]: # (2)
                        m += 1
                        
        return result      