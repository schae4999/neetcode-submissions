class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, curr = nums[0], 0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            best = max(best, curr)
        
        return best

                