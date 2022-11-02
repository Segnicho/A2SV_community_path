class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for passngr, start, end in trips:
            arr.append((start, passngr))
            arr.append((end, -passngr))
        # print(arr)
        arr.sort()
        # print(arr)
        pas = 0
        for tupl in arr:
            pas += tupl[1]
            if pas > capacity:
                return False
        return True
