class Solution:
    def isPalindrome(self, s: str) -> bool:
        strR = ""
        strL = ""

        for char in s:
            if char.isalnum():
                strL += char.lower()

        for char in s[::-1]:
            if char.isalnum():
                strR += char.lower()

        return (strL == strR)