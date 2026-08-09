class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l += 1
            else:
                r -= 1
        return l