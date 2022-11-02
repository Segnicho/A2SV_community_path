class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        count,res =0,math.inf
        while r < len(nums):
            count += nums[r]
            while count >= target and l<=r:
                res = min(res, r-l+1)
                count-=nums[l]
                l+=1
            r+=1
        return 0 if res == math.inf else res
