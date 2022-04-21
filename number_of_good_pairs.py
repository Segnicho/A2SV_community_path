# https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        for i in range (len(nums)-1):
            key = nums[i]
            for j in range (i+1, len(nums)):
                if key == nums[j] :
                    count+=1
        return count
