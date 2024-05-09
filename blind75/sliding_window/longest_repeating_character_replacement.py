class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # keep track of max char means you need to keep track of all char counts
        # to keep track of max in sliding window you need a way to remember 
        # everything in window so that you can update counts when window moves (counts for new window)
        
        longest = 0
        counts = {}
        l = 0
        max_char_count = 0
        
        for r, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1
            max_char_count = max(max_char_count, counts[c])
            current_len = r - l + 1
            
            if current_len - max_char_count <= k:
                longest = max(current_len, longest)
                
            else:
                while current_len - max_char_count > k and l < r:
                    counts[s[l]] -= 1
                    l += 1
                    max_char_count = max(counts.values())
                    current_len = r - l + 1
        
        return longest