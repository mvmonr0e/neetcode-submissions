class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        l = 0
        r = len(nums)-1
        
        while l < len(nums)-1:
            target = -(nums[l] + nums[r])
            if target in nums[l+1:r] and not [nums[l],target,nums[r]] in res:
                res.append([nums[l],target,nums[r]])
            
            r-=1
            if not l < r:
                l += 1
                r = len(nums)-1

        return res
            