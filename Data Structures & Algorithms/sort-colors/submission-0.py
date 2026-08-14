class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            curr = i
            while curr > 0 and nums[curr] < nums[curr-1]:
                # swap elements
                temp = nums[curr-1]
                nums[curr-1] = nums[curr]
                nums[curr] = temp

                # decrease the tracker of our current elem
                curr -= 1 
                #print(nums)

        