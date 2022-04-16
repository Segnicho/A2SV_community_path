class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) > 2:
            for i in range(len(intervals)-2):
                if intervals[i][1] >= intervals[i+1][0]:
                    if intervals[i][0] > intervals [i+1][0] and intervals[i][1] > intervals[i+1][1]:
                        intervals[i] = [intervals[i+1][0], intervals[i][1]]  
                    else:
                        intervals[i] = [intervals[i][0], intervals[i+1][1]]
                    intervals.pop(i+1)
            return intervals
        else:
            for i in range(len(intervals)-1):
                if intervals[i][1] >= intervals[i+1][0]:
                    if intervals[i][0] > intervals [i+1][0] and  intervals[i][1] > intervals[i+1][1]:
                        intervals[i] = [intervals[i+1][0], intervals[i][1]]  
                        # print("nnj")
                    else:
                        intervals[i] = [intervals[i][0], intervals[i+1][1]]
                    intervals.pop(i+1)
            return intervals
