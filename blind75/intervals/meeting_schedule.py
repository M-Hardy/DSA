from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda interval:interval.start)
        prevEnd = float('-inf')

        for m in intervals:
            if m.start < prevEnd:
                return False
            prevEnd = m.end

        return True
            