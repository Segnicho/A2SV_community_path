if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)
    lst.sort(reverse = True)
    def srt(lst):
        for i in range(len(lst)):
            if lst[i] > lst[i+1]:
                return lst[i+1]
    print(srt(lst))
    
