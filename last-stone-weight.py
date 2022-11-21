class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # print(y,x,stones)
            if x!=y:
                heapq.heappush(stones, y-x)
            else:continue
        # print(stones)
        if not stones: return 0
        if stones[0] == 0: return 0
        return -stones[0]

# 8 7 [4, 2, 1, 1]
# 8 7 [1, 4, 1, 1, 2]
# [1, 4, 1, 1, 2]
