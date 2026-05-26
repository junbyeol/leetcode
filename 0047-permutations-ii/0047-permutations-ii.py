class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permute_set = set()
        num_range = list(range(-10, 10))
        char_range = "abcdefghijklmnopqrstu"
        int_to_char = {k: v for k, v in zip(num_range, char_range)}
        char_to_int = {k: v for k, v in zip(char_range, num_range)}

        def encode(l: List[int]):
            return "".join([int_to_char[i] for i in l])

        def decode(enc: str):
            return [char_to_int[c] for c in enc]

        def dfs(visits: int, l: List[int]):
            if len(l) == len(nums):
                permute_set.add(encode(l))
                return

            for i in range(0, len(nums)):
                if (1<<i) & visits == 0 :
                    dfs(visits | (1<<i), l + [nums[i]])

        dfs(0, [])

        return list(map(decode, list(permute_set)))