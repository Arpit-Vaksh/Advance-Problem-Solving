class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        w_start = 0
        w_product =1
        ans = 0

        for w_end in range(len(nums)):
            w_product *= nums[w_end]

            if w_product < k:
                ans += w_end - w_start + 1
            else:
                while w_start <= w_end and w_product >= k:
                    w_product /= nums[w_start]
                    w_start += 1
                
                ans += w_end - w_start + 1
            
        return ans
