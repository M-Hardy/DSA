from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals = sorted(intervals, key=lambda i:i[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = res[-1]
            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                res.append(intervals[i])
        return res


    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals = sorted(intervals, key=lambda i:i[0])
        res = []
        cur = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                res.append(cur)
                cur = intervals[i]
        
        if not res or cur[0] > res[-1][1]:
            res.append(cur)
        else:
            res[-1][1] = max(cur[1], res[-1][1])
        
        return res