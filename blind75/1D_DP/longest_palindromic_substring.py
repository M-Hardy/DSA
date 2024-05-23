# cut execution time by half by just returning the 
# pointers for the palindrome string each time 
# instead of slicing and storing each palindromic
# substring on each iteration of checkPalindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        longestPointers = (0, 0)
        for i in range(len(s)):
            oddL, oddR = self.checkPalindrome(s, i, i)
            evenL, evenR = self.checkPalindrome(s, i, i+1)
            curMax = max(oddR-oddL+1, evenR-evenL+1)

            if curMax > maxLength:
                maxLength = curMax
                longestPointers = (oddL, oddR) if curMax == oddR-oddL+1 else (evenL, evenR)

        return s[longestPointers[0]:longestPointers[1]+1]

        
    def checkPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r] :
            l -= 1
            r += 1

        # both pointers incremented 1 extra beyond match 
        # by while-loop so must decrement
        l += 1
        r -= 1
        return (l,r)


    def longestPalindrome2(self, s: str) -> str:
        maxLength = 0
        longest = ""
        for i in range(len(s)):
            odd = self.checkPalindrome(s, i, i)
            even = self.checkPalindrome(s, i, i+1)
            curMax = max(len(odd), len(even))
            if curMax > maxLength:
                maxLength = curMax
                longest = odd if maxLength == len(odd) else even
        
        return longest

        
    def checkPalindrome2(self, s, mid, mid2):
        pal = ""

        while mid >= 0 and mid2 < len(s) and s[mid] == s[mid2] :
            pal = s[mid:mid2+1]
            mid -= 1
            mid2 += 1

        return pal 