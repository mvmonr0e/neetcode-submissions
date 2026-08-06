class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False      

        sCount = {}
        tCount = {}

        for c in s:
            if c in sCount:
                sCount[c] += 1
            else:
                sCount[c] = 1

        for c in t:
            if c in tCount:
                tCount[c] += 1
            else:
                tCount[c] = 1

        return sCount == tCount
