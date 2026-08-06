class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""

        for i in s:
            if i.isalpha() or i.isnumeric():
                temp += i.lower()
  
        return (temp==temp[::-1])