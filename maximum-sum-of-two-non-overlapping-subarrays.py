class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ps = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0: ps[i] = nums[i]
            else: ps[i] = nums[i] + ps[i-1]
        def findMax(arr, l1, l2):
            res = arr[l1+l2-1]
            mx1 = arr[l1-1]
            for i in range(len(arr)-l1-l2):
                s1 = arr[l1+i] - arr[i]
                s2 = arr[l1+l2+i] -arr[l1+i]
                mx1 = max(mx1, s1)
                res = max(res, mx1+s2)
            return res
        max1 = findMax(ps, firstLen, secondLen)
        max2 = findMax(ps, secondLen, firstLen)
        # print(max1, max2)
        return max(max1, max2)
      
