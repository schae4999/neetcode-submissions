class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        curr = None
        for num in nums:
            if num == curr:
                return True
            curr = num
        return False