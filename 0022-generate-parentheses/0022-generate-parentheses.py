class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_list = []

        def dfs(left_p, left_unclosed, s):
            if left_p == 0 and left_unclosed == 0:
                ans_list.append(s)
                return

            if left_p == 0:
                ans_list.append(s + ')' * left_unclosed)
                return

            dfs(left_p - 1, left_unclosed + 1, s + '(')

            if left_unclosed > 0:
                dfs(left_p, left_unclosed-1, s + ')')

        dfs(n, 0, "")

        return ans_list
