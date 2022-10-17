class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        currV = 0
        l = 0
        for i in range(k):
            if s[i] in vowels:
                currV += 1
        r = k
        numV = currV
        
        while r < len(s):
            if s[l] in vowels:
                if s[r] not in vowels:
                    currV -=1
            else:
                if s[r] in vowels:
                    currV+=1
            l+=1
            r+=1
            numV = max(currV, numV)
        return numV
    
