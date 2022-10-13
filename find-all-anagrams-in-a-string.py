class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans = []
        l = 0
        print(cnt)
        for r, c in enumerate(s):
            cnt[c] -= 1
            print(c,cnt[c],s[l],cnt[s[l]])
            while cnt[c] < 0:
                cnt[s[l]] += 1
                l += 1
            if r - l + 1 == len(p):
                print("now")
                ans.append(l)  
        return ans
