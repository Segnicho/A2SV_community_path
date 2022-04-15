class Solution:
    def sortSentence(self, s: str) -> str:
        arr = list(s.split(" "))
        ary = list(s.split(" "))
        i = 0
        while i < len(arr):
            word = arr[i]
            theNum = word[-1]
            num = eval(theNum)
            x = word[:-1]
            ary[num-1] = x
            i = i+1
        x = (" ").join(ary)
        return x
  
