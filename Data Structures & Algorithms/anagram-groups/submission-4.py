
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = []

        temp = ""
        for s in strs:
            temp = sorted(s)
            for bucket in buckets:
                if temp == sorted(bucket[0]):
                    temp = ""
                    bucket.append(s)
            if not temp == "":
                buckets.append([s])
        return buckets