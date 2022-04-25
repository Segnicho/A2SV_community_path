#https://leetcode.com/problems/powx-n/submissions/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        halfPowr = self.myPow(x, int(n/2))
        #if the n is even: the result would be halfPowr square
        if n%2 ==0:
            return halfPowr*halfPowr
        else:
            if n > 0: 
                return x*halfPowr*halfPowr
            else:
                return (halfPowr*halfPowr)/x
