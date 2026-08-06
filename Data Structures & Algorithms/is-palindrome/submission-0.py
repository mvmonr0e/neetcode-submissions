class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        r = ""

        for i in s:
            if i.isalpha() or i.isnumeric():
                l += i.lower()
        for i in reversed(s):
            if i.isalpha() or i.isnumeric():
                r += i.lower()

        print(l)
        print(r)       
        return (l==r)