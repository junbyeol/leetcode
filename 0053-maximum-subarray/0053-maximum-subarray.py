class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        for i, num in enumerate(nums):
            if i==0:
                dp.append(nums[i])
            else:
                dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))

        # print(dp)

        return max(dp)