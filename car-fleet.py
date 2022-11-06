class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for pos, spd in zip(position,speed):
            posSpeed.append([pos,spd])
        stk = []
        # print(posSpeed)
        for pos, spd in sorted(posSpeed)[::-1]:
            t = ((target-pos)/spd)
            stk.append(t)
            if len(stk)> 1 and stk[-2] >= stk[-1]:
                stk.pop()
        return len(stk) 
