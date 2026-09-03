class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, path, start):
            # base cases
            if (remaining == 0):
                result.append(path.copy())
                return
            
            if (remaining < 0):
                return

            for i in range(start, len(nums)):
                curr = nums[i]

                # choose
                path.append(curr)

                # explore
                backtrack(remaining - curr, path, i)

                # undo
                path.pop()

            return path
        
        backtrack(target, [], 0)

        return result


