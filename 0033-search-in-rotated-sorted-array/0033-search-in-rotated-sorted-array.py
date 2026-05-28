class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        def binary_search(l: List[int]):
            print(f'bin_search: {l}')
            lp = 0
            rp = len(l) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                print(f'l[{lp}] = {l[lp]}, l[{rp}] = {l[rp]}')
                if l[mid] == target:
                    return mid
                
                if target < l[mid]:
                    rp = mid - 1

                if l[mid] < target:
                    lp = mid + 1
                
            return -1

        while lp <= rp:
            l = nums[lp]
            r = nums[rp]
            print(f'nums[{lp}] = {l}, nums[{rp}] = {r}')

            if r < l:
                mid = (lp + rp) // 2
                if nums[mid] <= r:
                    if nums[mid] <= target <= r:
                        bs = binary_search(nums[mid:rp+1])
                        return bs + mid if bs != -1 else bs
                    else:
                        rp = mid - 1
                if l <= nums[mid]:
                    if l <= target <= nums[mid]:
                        bs = binary_search(nums[lp:mid+1])
                        return bs + lp if bs != -1 else bs
                    else:
                        lp = mid + 1
            else:
                bs = binary_search(nums[lp:rp+1])
                return bs + lp if bs != -1 else -1

        return -1