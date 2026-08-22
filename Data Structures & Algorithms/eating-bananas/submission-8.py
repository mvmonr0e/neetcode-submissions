class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            # calculate mid point
            k = (l+r) // 2
            # track total hours
            hourCount = 0
            
            # calculate total time to eat all bananas
            for p in piles:
                hourCount += (p+k-1) // k

            # search right of our current mid point if too many hours
            if hourCount <= h:
                res = k
                r = k -1
            # search left side if not enough hours
            else:
                l = k + 1
            
        return res

                