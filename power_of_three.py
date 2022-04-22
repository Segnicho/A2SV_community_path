# https://leetcode.com/problems/power-of-three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n ==3:
            return True
        elif n > 3:
            return self.isPowerOfThree(n/3)
        else:
            return False
