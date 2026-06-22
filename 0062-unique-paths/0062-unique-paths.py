class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = m + n - 2
        r = min(m,n) - 1
        res = 1
        for i in range(0, r):
            res = res * (s - i)

        for i in range(1, r+1):
            res = res // i

        return res