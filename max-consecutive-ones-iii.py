class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lptr = 0
        rptr = 0
        for rptr in range (len(nums)):
            if nums[rptr ] == 0:
                k-=1
            if k < 0:
                if nums[lptr ] == 0:
                    k+=1
                lptr +=1
        return rptr -lptr + 1
