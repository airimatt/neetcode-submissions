"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals) - 1):
            start, end = intervals[i].start, intervals[i].end
            start2, end2 = intervals[i + 1].start, intervals[i + 1].end
            if end > start2:
                return False
            

        return True