class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        for i in range(n-1):
            if i%2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i%2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
