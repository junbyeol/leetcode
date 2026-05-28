class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot_i = -1
        change_i = 0

        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot_i = i-1
                change_i = i
                
                for j in range(i, len(nums)):
                    if nums[pivot_i] < nums[j]:
                        change_i = j

                break

        print(f'pivot is {nums[pivot_i]}')
        print(f'change is {nums[change_i]}')

        if change_i != None:
            tmp = nums[pivot_i]
            nums[pivot_i] = nums[change_i]
            nums[change_i] = tmp

        nums[pivot_i+1:] = sorted(nums[pivot_i+1:])

        return nums


        