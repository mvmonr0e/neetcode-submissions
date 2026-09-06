class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        maxf = 0

        for r in range(len(s)):
            # update count of each char in s
            count[s[r]] = 1 + count.get(s[r], 0)
 
            # track the most frequent count
            if count[s[r]] > maxf:
                maxf = count[s[r]]

            # update left ptr while window is invalid
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # update result if window is valid
            # and larger than current result
            if (r-l+1) > res:
                res = r-l+1

        # return result
        return res