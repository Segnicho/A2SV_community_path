class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lptr = 0
        rptr = 0
        maxLen = 0
        diktn = {}
        for rptr in range(len(fruits)):
            diktn[fruits[rptr]] = rptr
            if len(diktn)>2:
                leftMost = min(diktn.values())
                del diktn[fruits[leftMost]]
                lptr=leftMost+1
            maxLen = max(maxLen, rptr-lptr+1)
        return maxLen
            
            
