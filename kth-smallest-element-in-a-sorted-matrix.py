class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
                flattenMatrix = [item for submatrix in matrix for item in submatrix] 
                heapq.heapify(flattenMatrix)
                i = 0
                while i < k:
                    kthSmallestEl = heapq.heappop(flattenMatrix)
                    i+=1
                return kthSmallestEl 
