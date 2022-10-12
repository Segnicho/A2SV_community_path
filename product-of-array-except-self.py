class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefx = 1
        for i in range(len(nums)):
            output[i]= prefx
            prefx*=nums[i]
        postfx = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *=postfx
            postfx *=nums[i]
        return output
