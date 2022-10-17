class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lptr= 0
        res = 0
        k = 1
        for rptr  in range(len(nums)):
            if nums[rptr] == 0:
                k -= 1
            while k < 0 and lptr <= rptr:
                if nums[lptr] == 0:
                    k += 1
                lptr += 1
            res = max(res,rptr-lptr)
        return res
