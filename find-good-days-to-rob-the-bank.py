class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        prefx = [0]
        sfx = [0]
        cnt = 0
        for i in range(1, n):
            if security[i-1] >= security[i]:
                cnt +=1 
            else:
                cnt = 0
            prefx.append(cnt)
        scnt = 0
        for i in range(n-2, -1, -1):
            if security[i+1] >= security[i]:
                scnt +=1
            else:
                scnt = 0
            sfx.append(scnt)
        sfx.reverse()
        res = []
        for i in range(n):
            if prefx[i] >= time and sfx[i] >= time:
                res.append(i)
        return res
