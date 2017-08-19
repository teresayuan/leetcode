# LeetCode - Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda i:i.start)

        merged_intervals = [intervals[0]]

        for i in intervals:
            if i.start <= merged_intervals[-1].end:
                merged_intervals[-1].end = max(merged_intervals[-1].end, i.end)
            else:
                merged_intervals.append(i)

        return merged_intervals


if __name__ == '__main__':
    a = Interval(2,3)
    b = Interval(2,2)
    c = Interval(3,3)
    d = Interval(1,3)
    e = Interval(5,7)
    f = Interval(2,2)
    g = Interval(4,6)
    x = [a, b, c, d, e, f, g]
    sol = Solution().merge(x)

    for s in sol:
     print (s.start, s.end)