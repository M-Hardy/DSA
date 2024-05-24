from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        maxCount = 0
        count = 0
        i = j = 0

        while i < len(end) and j < len(start):
            if start[j] < end[i]:
                count += 1
                j += 1
            # end >= start, means we have reached end of a meeting
            # so decrement count by 1 meeting and go to next meeting end
            else:  
                count -= 1
                i += 1

            maxCount = max(maxCount, count)
        
        return maxCount