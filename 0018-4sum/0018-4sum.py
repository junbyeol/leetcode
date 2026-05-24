class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_list = []
        nums.sort()
        print(nums)

        for i in range(0, len(nums) - 3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                valid_range = range(j+1, len(nums))
                lp = valid_range.start
                rp = valid_range.stop - 1
                print(f'iteration {nums[i]}({i}), {nums[j]}({j}), start with {nums[lp]}({lp}), {nums[rp]}({rp})')

                while lp in valid_range and rp in valid_range and lp < rp:
                    if nums[i] + nums[j] + nums[lp] + nums[rp] == target:
                        while lp+1 in valid_range and nums[lp] == nums[lp+1]:
                            lp = lp + 1
                        while rp-1 in valid_range and nums[rp] == nums[rp-1]:
                            rp = rp - 1
                        print(f'append: {[nums[i], nums[j], nums[lp], nums[rp]]}')
                        ans_list.append([nums[i], nums[j], nums[lp], nums[rp]])

                        lp = lp + 1
                        rp = rp - 1
                        continue

                    if nums[i] + nums[j] + nums[lp] + nums[rp] < target:
                        lp = lp + 1
                    else:
                        rp = rp - 1

        return ans_list

                