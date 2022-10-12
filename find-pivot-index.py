class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            nxt = left_sum + nums[i]
            right_sum = tot - nxt
            print(nxt)
            if right_sum == left_sum:
                return i
            left_sum = nxt
        return -1
