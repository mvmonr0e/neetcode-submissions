class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        areas = []
        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                areas.append(area)
                l += 1
            else:
                area = heights[r] * (r-l)
                areas.append(area)
                r -= 1
        return max(areas)
