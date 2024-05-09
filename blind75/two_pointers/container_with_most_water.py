class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most_water = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            current = min(height[l], height[r]) * (r-l)
            most_water = max(current, most_water)
            
            if height[l] < height[r]:
                l += 1
            
            else: 
                r -= 1
                
        return most_water