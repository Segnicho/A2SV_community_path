class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            ans=0
            prefsum=0
            d={0:1}

            for i in range(len(nums)):
                prefsum = prefsum + nums[i]
                ans += d.get(prefsum-k,0)
                # if prefsum-k in d:
                    # ans = ans + d[prefsum-k]
                if prefsum not in d:
                    d[prefsum] = 1
                else:
                    d[prefsum] = d[prefsum]+1

            return ans
