class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = sum(arr[:k])
        threshold *= k
        count = 0        
        if currSum >= threshold:
            count = 1
        for i in range(len(arr)-k):
            currSum += arr[i+k] - arr[i]
            if currSum >= threshold:
                count+=1
        return count
