class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:  
        totl = sum(cardPoints)
        smlSubArray = len(cardPoints) - k
        currSum = sum(cardPoints[:smlSubArray])
        res = currSum
        j = 0
        for i in range(smlSubArray,len(cardPoints)):
            currSum += cardPoints[i]
            currSum -=  cardPoints[j]
            j+=1
            res = min(currSum, res)
        return totl-res
    
