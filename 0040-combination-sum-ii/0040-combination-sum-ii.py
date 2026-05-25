class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans_dict = []
        candidates.sort()

        def dfs(p_candi, l, goal):
            if goal == 0:
                ans_dict.append(l)
                return

            if p_candi >= len(candidates):
                return

            now_candi = candidates[p_candi]
            if goal >= now_candi:
                dfs(p_candi + 1, l + [now_candi], goal - now_candi)
            
            while p_candi + 1 < len(candidates) and now_candi == candidates[p_candi+1]:
                p_candi = p_candi + 1
            dfs(p_candi + 1, l, goal)

        dfs(0, [], target)

        return ans_dict

                