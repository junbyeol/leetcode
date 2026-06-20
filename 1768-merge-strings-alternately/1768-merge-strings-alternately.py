class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        res = ""
        for i in range(0, max_len):
            if i < len(word1):
                res = res + word1[i]
            if i < len(word2):
                res = res + word2[i]
        return res