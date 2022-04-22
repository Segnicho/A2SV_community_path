# https://leetcode.com/problems/reduce-array-size-to-the-half/submissions/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ls = []
        size = len(arr)
        for element in arr:
            if element not in ls:
                ls.append(element)
        for element in ls:
            occurence = arr.count(element)
            temp = ls.index(element)
            ls.pop(temp)
            ls.insert(temp, [occurence, element])
        ls.sort(reverse=True)
        count = 0
        lessSize = 0
        for i in range(len(ls)):
            if ls[i][0] >= size//2:
                count+=1
                return count
            else:
                lessSize += ls[i][0]
                count+=1
                if lessSize >= size//2:
                    return count
                
           
