class Solution:
    MAX = float('inf')
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        dp = [[self.MAX for _ in range(w)] for _ in range(h)]

        for i, _ in enumerate(dp):
            for j, _ in enumerate(dp[i]):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[h-1][w-1]