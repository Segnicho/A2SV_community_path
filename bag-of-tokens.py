class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        l , r = 0 , len(tokens)-1
        ans = 0
        while l <= r:
            if tokens[l] <= power:
                score+=1
                ans =max(ans, score)
                power -= tokens[l]
                l += 1
            elif score >= 1:
                score-=1
                power+= tokens[r]
                r-=1
            else:break
        return ans
