class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # monotonic property: as k increases, total_hours can only decrease / stay the same
        # binary search through possible k
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / mid)
            
            if total_hours <= h:
                # it works but might not be the minimum
                right = mid - 1
            else:
                # since it doesn't work, should increase k
                left = mid + 1

        return left