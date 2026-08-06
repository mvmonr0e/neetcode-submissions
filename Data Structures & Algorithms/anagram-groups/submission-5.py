def isAnagram(s, t):
        sMap = {}
        for c in s:
            sMap[c] = 1 + sMap.get(c, 0)

        tMap = {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        return sMap == tMap
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = []

        temp = ""
        for s in strs:
            temp = sorted(s)
            for bucket in buckets:
                if not bucket == [] and isAnagram(s,bucket[0]):
                    temp = ""
                    bucket.append(s)
            if not temp == "":
                buckets.append([s])
        return buckets