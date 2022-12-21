class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}

        for i in range(len(s)):
            if s[i:i+10] not in hashmap:
                hashmap[s[i:i+10]] = 0
            hashmap[s[i:i+10]] += 1

        return [key for key,value in hashmap.items() if value > 1]
