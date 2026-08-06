class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMapS = {}
        countMapT = {}

        for c in s:
            if c in countMapS:
                countMapS[c] += 1
            else:
                countMapS[c] = 1
            
        
        for c in t:
            if c in countMapT:
                countMapT[c] += 1
            else:
                countMapT[c] = 1

        return countMapS == countMapT