class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right  = len(nums) - 1
        
        while(right >= left): 
            mid = (right - left) // 2
            mid += left
            if nums[mid] == target: 
                return mid
            elif target > nums[mid]: 
                left += 1 
            else: 
                right -= 1 
        
        return -1 