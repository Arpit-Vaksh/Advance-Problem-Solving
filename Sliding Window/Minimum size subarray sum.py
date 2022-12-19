class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ws=0
        wsum=0
        minlen = float("inf")
        for we in range(len(nums)):
            wsum+=nums[we]

            while wsum>=target:
                minlen=min(minlen,we-ws+1)
                wsum-=nums[ws]
                ws+=1
        if minlen == math.inf: #or float("inf") : same thing
            return 0
        return minlen
