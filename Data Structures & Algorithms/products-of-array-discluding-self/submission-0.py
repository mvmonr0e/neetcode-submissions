class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        for i, n in enumerate(nums):
            temp = nums[:i] + nums[i+1:]
            prod = 1
            for t in temp:
                prod *= t
            prods.append(prod)
        return prods
            
                
