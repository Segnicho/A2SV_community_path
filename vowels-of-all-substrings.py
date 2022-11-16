class Solution:
    def countVowels(self, word: str) -> int:
        vows = ('a', 'e', 'i','o','u')
        n = len(word)
        res = 0 
        for ind, ch in enumerate(word):
            chOccurrance = 0
            if ch in vows:
                chOccurrance = (n-ind)*(ind+1)
                res+=chOccurrance
        return res

