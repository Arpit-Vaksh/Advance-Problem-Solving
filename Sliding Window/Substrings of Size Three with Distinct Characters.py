class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            w = set(s[i:i+3])
            if len(w) == 3:
                ans += 1
        return ans
