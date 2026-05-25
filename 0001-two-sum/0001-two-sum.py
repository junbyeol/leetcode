class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i_dict = {}

        for i, num in enumerate(nums):
            goal = target - num
            if goal in num_i_dict:
                return [i, num_i_dict[goal]]
            num_i_dict[num] = i

        # return []
                