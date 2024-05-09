class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        found = {}    
        max_substring = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in found and found[s[r]] >= l:
                l = found[s[r]] + 1
        
            found[s[r]] = r
            max_substring = max(max_substring, r-l+1)
            
        return max_substring