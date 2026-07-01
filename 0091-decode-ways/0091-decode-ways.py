class Solution:
    def numDecodings(self, s: str) -> int:
        hashmap = {}

        def rec(s: str) -> int:
            if s in hashmap:
                return hashmap[s]

            if s.startswith("0"):
                return 0
            
            if len(s) <= 1:
                return 1
            
            if s.startswith("1") or s[:2] in ["20", "21", "22", "23", "24", "25", "26"]:
                res = rec(s[1:]) + rec(s[2:])
                hashmap[s] = res
                return hashmap[s]

            hashmap[s] = rec(s[1:])
            return hashmap[s]
        
        return rec(s)
        