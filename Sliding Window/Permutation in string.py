class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map = {}
        
        for ch in s1:
            map[ch] = map.get(ch,0)+1
        
        w_start = 0
        matched = 0

        for w_end in range(len(s2)):
            curr_char = s2[w_end]

            if curr_char in map:
                map[curr_char] -= 1
                if map[curr_char] == 0:
                    matched += 1
                
            if matched == len(map):
                return True
            
            if w_end >= len(s1) - 1:
                leftchar = s2[w_start]
                w_start += 1

                if leftchar in map:
                    if map[leftchar] == 0:
                        matched -= 1
                    map[leftchar] += 1
                
        return False
 
