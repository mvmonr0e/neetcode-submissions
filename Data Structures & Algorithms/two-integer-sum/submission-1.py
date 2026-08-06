class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force

        for i,n in enumerate(nums):
            temp = i
            for j in nums[i+1:]:
                temp = temp + 1
                if n + j == target:
                    return [i,temp]

        return