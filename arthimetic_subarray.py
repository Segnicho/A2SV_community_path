class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arr = []
        for i,_ in enumerate(l):
            temp = sorted(nums[l[i]:r[i]+1])
            temp = set( temp[i]-temp[i-1] for i in range(1,len(temp)))
            arr.append( len(temp) == 1 )
        return arr
            
            # arry = ["true", "true", "true"]
            # nums.sort()
            # d = nums[1]-nums[0]
            # for i in range (1,len(nums)-1):
            #     if nums[i] != (nums[0] + i*d):
            #         arry.pop(0)
            #         arry.insert(0,"false")    
            #         break
            # l.sort()
            # b = (l[-1]-l[0])/(len(l)-1)
            # for i in range (1,len(l)-1):
            #     if l[i] != (l[0] + i*b):
            #         arry.pop(1)
            #         arry.insert(1,"false")       
            #         break
            # r.sort()
            # c = r[1]-r[0]
            # for i in range (1,len(r)-1):
            #     if (r[i] != (r[i] + i*c)):
            #         arry.pop(2)
            #         arry.insert(2,"false")
            #         break
            # rr = []
            # for elmnt in arry:
            #     if elmnt == "true":
            #         rr.append(True)
            #     else:
            #         rr.append(False)
            # return rr
