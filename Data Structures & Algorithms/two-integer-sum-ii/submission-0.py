class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]

            # if sum too small, move l to right
            elif curr_sum < target:
                l += 1
            
            # if sum too big, move r to left
            elif curr_sum > target:
                r -= 1


            

