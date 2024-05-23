class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0                 
        for i in range(len(s)):
            odd = self.checkPalindrome(s, i, i)
            even = self.checkPalindrome(s, i, i+1)
            total += odd + even
        return total
    
    def checkPalindrome(self, s, l, r):
        pals = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pals += 1
            l -= 1
            r += 1
        return pals