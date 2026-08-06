class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxA = (r-l)*min(heights[l],heights[r])

        while l < r:
            tempA = (r-l)*min(heights[l],heights[r])
            if tempA > maxA:
                maxA=tempA

            if max(heights[l],heights[r]) == heights[l]:
                r-=1
            else:
                l+=1
                
            

        return maxA