class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        res = 0
        lptr = 0
        mnt = False
        n = len(arr)
        for i in range(1, len(arr)-1):
            #if you come across mountain flag mount true
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                mnt = True
            # if you come across the lowest point update update result
            elif arr[i-1] >= arr[i] and arr[i] <= arr[i+1]:
                #  if we came across mountain update result
                if mnt:
                    res = max(res, i-lptr+1)
                    mnt = not mnt
                lptr = i
        #if you finished walking down the alley: compare this mountain and the highest till now
        if mnt and arr[n-1] < arr[n-2]:
            res = max(res, n-lptr)
        return res
