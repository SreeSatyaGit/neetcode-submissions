class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        count = 0

        for start,end in intervals[1:]:
            if start >= prev[1]:
                prev[1] = max(prev[1],end)
            else:
                count+=1
                prev[1] = min(prev[1],end)
        return count