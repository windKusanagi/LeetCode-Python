# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # To print the result
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

class Solution(object):
     def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        result.append(intervals[0])
        for interval in intervals[1:]:
            prev = result[-1]
            if prev.end >= interval.start:
                prev.end = max(prev.end, interval.end)
            else:
                result.append(interval)
        return result
intervals = Solution().insert([Interval(2, 6), Interval(8, 10), Interval(15, 18)], Interval(13, 16))
for interval in intervals:
    print(interval)