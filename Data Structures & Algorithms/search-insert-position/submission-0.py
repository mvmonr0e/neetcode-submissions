class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if l == r:
                return l
            elif target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l += 1
            elif target < nums[mid]:
                r -= 1
        return -1