# for dp solution, idea is to start at what the end solution would 
# be, and then build intermediate solutions backward from there till 
# you reach the start, then when you hit the start verify if you can 
# reach the end case from the start point by using the pre-solved 
# intermediate solutions 

from typing import List

class Solution:
    # dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #stores if rest of word can be made from wordDict at s[i]
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # end solution (base case)

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # if there is a word that fits in s and matches at s[i]
                # can make rest of word if it hits len(s) or if s[i] it connects to hits len(s)
                if i + len(w) <= len(s) and s[i: i+len(w)] == w: 
                    #set true if there is a word that connects to an s[i] where rest of word can be made
                    if dp[i] == False:
                        dp[i] = dp[i+len(w)] 
        
        return dp[0]


    #correct - not dp, dfs with memoization
    def DFS_MEMO_wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set() #(index, traversed branch)
        return self.helper(s, wordDict, "", 0, cache)

    def helper(self, s, wordDict, cur, i, cache):
        if (i, cur) in cache:
            return False
        
        cur += s[i]
        if cur in wordDict:
            if i+1 >= len(s):
                return True
            if self.helper(s, wordDict, "", i+1, cache) or self.helper(s, wordDict, cur, i+1, cache):
                return True
            else:
                cache.add((i, cur))
                
        else:
            if i+1 >= len(s):
                return False
            if self.helper(s, wordDict, cur, i+1, cache):
                return True
            else:
                cache.add((i, cur))
            

    #DFS no memoization - TLE
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, "")
        
    def helper2(self, s, wordDict, cur):
        cur += s[0]
        if cur in wordDict:
            if len(s) == 1:
                return True
            else:
                return self.helper(s[1:], wordDict, "") or self.helper(s[1:], wordDict, cur)
        else:
            if len(s) == 1:
                return False
            else:
                return self.helper(s[1:], wordDict, cur) 