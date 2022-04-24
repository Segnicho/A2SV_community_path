class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        for str in nums:
            arr.append(eval(str))
        arr.sort(reverse = True)
        num = arr[k-1]
        return f"{num}"
