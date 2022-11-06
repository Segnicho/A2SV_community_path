class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        dikt = {}
        for num in nums:
            if k - num in dikt and dikt[k-num] > 0:
                res+=1
                dikt[k-num] -=1
            else:dikt[num] = dikt.get(num,0) +1
            # elif num not in dikt:
            #     dikt[num] =1
            # else:
            #     dikt[num] +=  1   
        return res
