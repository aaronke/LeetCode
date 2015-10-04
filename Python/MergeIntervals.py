# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals = sorted(intervals, key=self.sort_key)
        i = 0
        # merge in place, del the position dynamically update index
        while i < len(intervals)-1:
            end = intervals[i].end
            while i+1 < len(intervals) and intervals[i+1].start <= end:
                end = max(end, intervals[i+1].end)
                del intervals[i+1]
            intervals[i] = Interval(intervals[i].start, end)
            i += 1
        return intervals
        
    def sort_key(self, interval):
        return interval.start
