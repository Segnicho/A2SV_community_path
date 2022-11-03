class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        Mod =  10**9+7
        arr.sort()
        i = 0
        ans = 0
        while  i < len(arr):
            newT = target - arr[i] 
        #use two sum method from now on
            j = i+1
            k = len(arr)-1
            while j<k:
                
                if arr[j] + arr[k] < newT:
                    j+=1
                elif arr[j] + arr[k] > newT:
                    k-=1
                elif arr[j] != arr[k]:
                #the two numbers are different and let's count them
                    lcount = 1
                    rcount = 1
                    while j+1 < k and arr[j] == arr[j+1]:
                        lcount +=1
                        j+=1
                    while k-1 > j and arr[k] == arr[k-1]:
                        rcount +=1
                        k-=1
                    ans += (lcount*rcount)
                    ans%=Mod
                    j+=1
                    k-=1
                else:
                    #n/2(n+1)
                    ans += (k-j+1)*(k-j)//2
                    ans%=Mod
                    break
            i+=1
        return ans
