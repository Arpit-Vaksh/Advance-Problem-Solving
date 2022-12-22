class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        w_start = 0
        ans = 0
        curr_sum = 0
        nums.sort()
        for w_end in range(len(nums)):
            curr_sum += nums[w_end]

            while nums[w_end]*(w_end - w_start + 1) > curr_sum+k :
                curr_sum -= nums[w_start]
                w_start += 1

            ans = max(ans, w_end - w_start +1)

        return ans
