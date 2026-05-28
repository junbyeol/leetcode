class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s: str):
            ans = ""
            this_chunk = ""
            for i in range(0, len(s)):
                if len(this_chunk) == 0 or this_chunk[-1] == s[i]:
                    this_chunk += s[i]
                else:
                    ans += str(len(this_chunk))
                    ans += this_chunk[-1]
                    this_chunk = s[i]

            ans += str(len(this_chunk))
            ans += this_chunk[-1]
            return ans

        res = "1"
        for _ in range(1,n):
            res = rle(res)
        return res
