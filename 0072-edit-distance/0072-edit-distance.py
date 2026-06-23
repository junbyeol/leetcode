class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h = len(word1)+1
        w = len(word2)+1
        dp = [[_ for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if i == 0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

        return dp[h-1][w-1]


        