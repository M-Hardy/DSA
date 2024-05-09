class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        found = set()
        for num in nums:
            if num in found:
                return True
            found.add(num)
            
        return False