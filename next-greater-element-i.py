class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        stk = []
        res = []
        stk.append(nums2[0])
        dikt = {}
        for i in range(1, len(nums2)):
            while stk and nums2[i] > stk[-1]:
                dikt[stk[-1]] = nums2[i]
                stk.pop()
            stk.append(nums2[i])
        return [dikt.get(n, -1) for n in nums1]
    
