class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wCount = {}
        for word in words:
            wCount[word] = wCount.get(word,0)+1
        sorted_wCount = {val[0] : val[1] for val in sorted(wCount.items(), key = lambda x: (-x[1], x[0]))}
        res = []
        i = 0
        for ky, val in sorted_wCount.items() :
            res.append(ky)
            i+=1
            if i == k:
                return res
