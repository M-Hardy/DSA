class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if interval ends before new one starts add it 
            # to result array (no merge required)
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # if interval starts after new one ends, add our 
            # new one and then return concatenated res + remaining 
            # intervals in problem array
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                # we iterate with i so we can return using array slice 
                return res + intervals[i:] 

            # if beginning/end of new interval intersects with current 
            # interval, merge them
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]), 
                    max(intervals[i][1], newInterval[1])
                ]

        # if we do not short circuit in the loop, 
        # we did not find an interval that starts after
        # the new interval ends (there is no interval after
        # our new interval). 
        #  in this case, our new interval is the last one 
        # in the set and needs to be added at the end
        res.append(newInterval)
        return res