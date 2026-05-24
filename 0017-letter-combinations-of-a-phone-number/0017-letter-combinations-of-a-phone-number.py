class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans_list = []
        digit_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u', 'v'],
            '9': ['w','x','y','z'],
        }

        def dfs(idx, s):
            if idx == len(digits):
                ans_list.append(s)
                return
            
            for c in digit_map[digits[idx]]:
                dfs(idx+1, s + c)

        dfs(0, "")

        return ans_list
