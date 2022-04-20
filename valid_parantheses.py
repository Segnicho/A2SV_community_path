class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(", "[", "{"]
        cp = [")", "]", "}"]
        arr = []
        for par in s:
            if par in op:
                arr.append(par)
            elif par in cp:
                indx = cp.index(par)
                if len(arr)>=1 and  op[indx] == arr[len(arr)-1]:
                    arr.pop()
                else:
                    return False
        return len(arr) == 0
