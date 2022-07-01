class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [None]*len(nums)
        for j in range (k):
            for i in range (len(nums)):
                arr[i] = nums[i-1]
            nums[:] = arr[:]
        return arr
