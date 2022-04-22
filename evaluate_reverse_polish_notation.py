# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', "/", "*"]
        stck = []
        ans = 0
        for i in range (len(tokens)):
            if len(tokens) == 1:
                    return eval(tokens[0])
            if tokens[i] not in operators:
                stck.append(eval(tokens[i]))
            
            else:
                temp1 = stck.pop(-1)
                temp2 = stck.pop(-1)
                if tokens[i] =='+':
                    ans = temp2 + temp1
                if tokens[i] =='-':
                    ans = temp2 - temp1
                if tokens[i] =='/':
                    ans = int(float(temp2) / temp1)
                if tokens[i] =='*':
                    ans = temp2 * temp1
                stck.insert(i-2, ans)
        return ans
