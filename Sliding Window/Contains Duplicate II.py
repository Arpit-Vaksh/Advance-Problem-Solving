class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for w_end in range(len(nums)):
            if ( nums[w_end] in d and abs( d[nums[w_end]] - w_end) <= k):
                return True
            d[nums[w_end]] = w_end

        return False
