class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        mult = 1
        for n in nums:
            mult *= n
            pre.append(mult)

        post = []
        mult = 1
        for n in nums[::-1]:
            mult *= n
            post.append(mult)
        post = post[::-1]

        ans = []
        for i,n in enumerate(nums):
            if i == 0:
                ans.append(post[1])
            elif i == len(nums)-1:
                ans.append(pre[len(pre)-2])
            else:
                ans.append(pre[i-1]*post[i+1])

        print(pre)
        print(post)
        return ans