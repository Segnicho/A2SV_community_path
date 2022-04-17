#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        key  = arr[i]   
    def selectionSort(self, arr,n):
        #code here
        for i in range (len(arr)):
            key = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[key]:
                    key = j
            arr[i], arr[key] = arr[key], arr[i]
        return arr
