class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        count = 1
        temp = []
        res = 0
        print(nums)
        for num in nums:
            print(num, end = " ")
            if temp == []:
                print('temp was empty so skipped')
                temp.append(num)
                continue
            if num == temp[-1]:
                print("was equal to end of temp")
            elif num == (temp[-1] + 1) or num == (temp[-1] - 1):
                print('added to temp')
                temp.append(num)
            else:
                print('resetting temp')
                print(temp)
                temp = [num]
            print(temp)
            res = max(res,len(temp))
        
        return res
        