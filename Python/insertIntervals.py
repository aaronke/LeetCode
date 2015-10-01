# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Binary search version, lg(n)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return [newInterval]
        low_index = self.bs_s(intervals, newInterval)
        high_index = self.bs_e(intervals, newInterval)
        # adjust boundry, to merge it or not
        if intervals[low_index].end < newInterval.start:
            low_index += 1
        if intervals[high_index].start > newInterval.end:
            high_index -= 1
        # some need to merge
        if low_index <= high_index:
            lower = min(newInterval.start, intervals[low_index].start)
            higher = max(newInterval.end, intervals[high_index].end)
            newInterval = Interval(lower, higher)
        for i in range(low_index, high_index+1):
            del intervals[low_index]
        intervals.insert(low_index, newInterval)
        return intervals

    def bs_s(self, intervals, newInterval):
        """
        return the lower index for the start point
        SPECIAL CASE, -1, up grade to 0
        """
        left, right = 0, len(intervals)-1
        while left <= right:
            mid = (left + right) / 2
            if intervals[mid].start > newInterval.start:
                right = mid - 1
            elif intervals[mid].start < newInterval.start:
                left = mid + 1
            else:
                return mid
        return max(0,min(left,right))
        
    def bs_e(self, intervals, newInterval):
        """
        return the higher index for end point
        SPECIAL CASE, len(list), down grade to len(list) - 1
        """
        left, right = 0, len(intervals)-1
        while left <= right:
            mid = (left + right) / 2
            if intervals[mid].end > newInterval.end:
                right = mid - 1
            elif intervals[mid].end < newInterval.end:
                left = mid + 1
            else:
                return mid
        return min(max(left,right),len(intervals)-1)
