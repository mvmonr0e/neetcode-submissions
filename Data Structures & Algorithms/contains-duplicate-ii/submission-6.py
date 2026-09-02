class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            j = i+k
            while j > len(nums)-1:
                j -= 1
            for x in range(i+1,j+1,1):
                if nums[i] == nums[x] and abs(i-x) <= k:
                    return True
        return False