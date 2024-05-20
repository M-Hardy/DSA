# *review this problem
# did not identify the recursive case - i think stumbling point
# was that i did not know how to implement making 2 branching choices
# at each iteration w.r.t dfs

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i, total + candidates[i], cur)
            
            cur.pop()
            dfs(i+1, total, cur)
        
        dfs(0, 0, [])
        return res