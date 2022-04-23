#https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        nums.sort()
        findex = nums.index(target)
        ans = [findex]
        if findex != (len(nums)-1):
            for i in range((findex+1),  len(nums)):
                if nums[i] == target:
                           ans.append(i)
        return ans
