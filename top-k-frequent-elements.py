class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        # nums.sort()
        for num in nums:
            if num not in arr:
                arr.append(num)
            else:
                continue
        ls =[]
        # print(arr)
        for element in arr:
            countr = nums.count(element)
            ls.append([countr, element])
        ls.sort(reverse=True)
        answer = []
