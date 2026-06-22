class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        max_x = len(obstacleGrid)
        max_y = len(obstacleGrid[0])
        dp = [[0 for _ in range(0, max_y)] for _ in range(0, max_x)]

        for x in range(0, max_x):
            for y in range(0, max_y):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0

                elif x == 0 and y == 0:
                    dp[x][y] = 1

                elif x == 0:
                    dp[x][y] = dp[x][y-1]
                
                elif y == 0:
                    dp[x][y] = dp[x-1][y]

                else:
                    dp[x][y] = dp[x][y-1] + dp[x-1][y]



        return dp[max_x - 1][max_y - 1]