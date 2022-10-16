class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        ans = []
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            lastEl = ans[-1][1]
            if intervals[i][0]<=lastEl :
                ans[-1][1] = max(lastEl,intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans
                
