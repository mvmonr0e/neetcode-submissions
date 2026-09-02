class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i,n in enumerate(nums):
            if n in seen:
                if abs(seen[n] - i) <= k:
                    return True
                else:
                    seen[n] = i
            else:
                seen[n] = i
            #print(seen)
        return False