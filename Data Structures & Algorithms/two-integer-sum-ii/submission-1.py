class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}

        for i,n in enumerate(numbers):
            diff = target - n
            if not diff in nums:
                nums[n] = diff
            else:
                return [numbers.index(diff)+1,i+1]
            