class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1"
        
        res = ""
        for i, s in enumerate(strs):
            if i == len(strs)-1:
                res += s
                break
            res += s + "`"
        return res

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []

        print(s)
        result = [""]
        i = 0
        for c in s:
            if c == "`":
                i += 1
                result.append("")
                continue
            result[i] += c
        return result

