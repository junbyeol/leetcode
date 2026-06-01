class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1,101)]
        dp = [-1] * 10001

        for num in range(1, n+1):
            if num in squares:
                dp[num] = 1
            else:    
                min_val = dp[num-1] + 1
                it = 1
                while squares[it] < num:
                    min_val = min(dp[num - squares[it]] + 1, min_val)
                    it = it + 1
                
                dp[num] = min_val

            # print(f'num: {num}, dp[num]: {dp[num]}')

        return dp[n]