class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hourCount = 0
            
            for p in piles:
                hourCount += (p+k-1) // k

            if hourCount <= h:
                res = k
                r = k -1
            else:
                l = k + 1
            
        return res

                