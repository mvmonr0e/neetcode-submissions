class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                maxArea = max(area,maxArea)
                l += 1
            else:
                area = heights[r] * (r-l)
                maxArea = max(area,maxArea)
                r -= 1
        return maxArea
