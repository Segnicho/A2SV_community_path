class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            count[num] = 1 + count.get(num,0)
        count = dict(sorted(count.items(), key= lambda item: item[1],reverse = True))
        target = len(arr)/2
        k = 0
        tot = 0
        for num, cnt in count.items():
            tot+=cnt
            k+=1
            if tot >= target:
                return k
