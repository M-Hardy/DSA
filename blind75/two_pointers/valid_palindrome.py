# isPalindrome:
# approach: compare parsed string (only alnum chars) with reversed string

# isPalindrome2:
# Just be careful with the while conditions for moving the start
# and end chars, specify the condition as the second-last char
# both ways cause while-loop executes one more time after condition 
# is passed (not like for-loop)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new = ''
        for c in s:
            if c.isalnum():
                new += c.lower()
        
        return new == new[::-1]
        
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        start = 0
        end = len(s) - 1
        
        while start < end:
            while not s[start].isalnum() and start < len(s) - 1:
                start += 1
            
            while not s[end].isalnum() and end > 0:
                end -= 1
        
            if start >= end: 
                return True
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True