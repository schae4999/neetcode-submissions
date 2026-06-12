class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, e = 0, len(heights) - 1
        max_area = 0

        while s < e:
            curr = min(heights[e], heights[s]) * (e - s)
            max_area = max(curr, max_area)
            
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1

        return max_area
