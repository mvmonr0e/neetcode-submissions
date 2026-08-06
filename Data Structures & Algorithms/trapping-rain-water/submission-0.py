class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL = []
        maxR = []

        maxi = 0
        for h in height:
            if h > maxi:
                maxi = h
            maxL.append(maxi)

        maxi = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > maxi:
                maxi = height[i]
            maxR.insert(0,maxi)

        for i,h in enumerate(height):
            diff = min(maxL[i],maxR[i]) - h
            if diff > 0:
                res += diff
        return res



