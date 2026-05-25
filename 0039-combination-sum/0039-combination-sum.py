class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans_dict = []

        def dfs(p_candi, l, goal):
            if goal == 0:
                ans_dict.append(l)
                return

            now_candi = candidates[p_candi]
            if goal >= now_candi:
                dfs(p_candi, l + [now_candi], goal - now_candi)
            
            if p_candi + 1 < len(candidates):
                dfs(p_candi + 1, l, goal)

        dfs(0, [] , target)

        return ans_dict

                