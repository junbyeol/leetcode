class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)

        # -4 -1 1 2
        closest_s = nums[0]+nums[1]+nums[2]

        for i, num in enumerate(nums[:-2]):
            lp = i+1
            rp = len(nums) - 1
            # print(f'iterate {i}:')

            # print(f'{lp} {rp}')
            while lp < rp:
                s = num + nums[lp] + nums[rp]

                # if new sums with new pointer are farther than the old
                # break loop
                if abs(target - s) < abs(target - closest_s):
                    closest_s = s

                if s < target:
                    lp = lp + 1
                else:
                    rp = rp - 1
                # print(f'{lp} {rp}')
                
            # print(f'best: sum={s} closest_s={closest_s}')

        return closest_s
                