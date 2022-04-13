class Solution:
    """
    i am going to create new list of square of the disance of the point from the origin to a list
    and  store index of these minimum numbers to get the closest points.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        #here i store the square of the distance of the points from the origin.
        for i in points:
            arr.append((i[0]*i[0]) + (i[1] *i[1]))
        n = 0
        ary = []
        #in this list i am going to store the index of the closest points.
        while n < k:
                ary.append(arr.index(min(arr)))
                arr.pop(arr.index(min(arr)))
                n+=1 
        for j in ary:
                    #since the order doesn't matter i am going to append the list to ary[0]
                    ary[0] = points[j]
        return ary
