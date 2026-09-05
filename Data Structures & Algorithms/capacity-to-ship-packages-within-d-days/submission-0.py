class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            mid = (l+r) // 2

            curr_boat = 0
            total_boats = 1
            for w in weights:
                if curr_boat + w <= mid:
                    curr_boat += w
                else:
                    total_boats += 1
                    curr_boat = w
            
            if total_boats > days:
                l = mid + 1
            elif total_boats <= days:
                r = mid - 1
                res = mid

        return res
