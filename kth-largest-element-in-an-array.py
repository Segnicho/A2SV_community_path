class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        i=0
        while i < k:
            lrgst = -heapq.heappop(nums)
            i+=1
        return lrgst
        
