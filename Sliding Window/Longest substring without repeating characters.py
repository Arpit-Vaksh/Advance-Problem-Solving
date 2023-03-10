class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w_start=0
        count={}
        maxlen=0
        for w_end in range(len(s)):
            count[s[w_end]] = count.get(s[w_end],0) + 1
            while count[s[w_end]]>1:
                count[s[w_start]] -= 1
                w_start += 1
            maxlen = max(maxlen, w_end - w_start + 1)

        return maxlen
