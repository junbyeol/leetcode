class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permute_set = list()

        def dfs(visits: int, l: List[int]):
            if len(l) == len(nums):
                permute_set.append(l)
                return

            for i in range(0, len(nums)):
                if (1<<i) & visits == 0 :
                    dfs(visits | (1<<i), l + [nums[i]])

        dfs(0, [])

        return list(permute_set)