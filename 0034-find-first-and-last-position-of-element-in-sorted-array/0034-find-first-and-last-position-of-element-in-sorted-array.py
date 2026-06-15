class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(mode) -> int: # mode: 0(left bound), 1(right bound)
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # print(f"{left}~{mid}~{right}")
                
                if nums[mid] == target:
                    if mode == 1:
                        if mid + 1 >= len(nums) or nums[mid+1] != target:
                            return mid
                        else:
                            left = mid + 1

                    if mode == 0:
                        if mid - 1 < 0 or nums[mid-1] != target:
                            return mid
                        else:
                            right = mid - 1

                if nums[mid] < target:
                    left = mid + 1

                if nums[mid] > target:
                    right = mid - 1

            # print(f"{left}~{right}")
            return -1

        return [binary_search(0), binary_search(1)]