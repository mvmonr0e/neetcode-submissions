class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        # encoded str formatted as length followed by delimiter then the str itself
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i

            # find the delimiter
            while s[j] != '#':
                j += 1
            
            # find the length using the position of the delimiter
            length = int(s[i:j])

            # find the beginning and end of the str
            i = j + 1
            j = i + length

            # append the string to the result
            res.append(s[i:j])

            # set i to the postition of the next strings length
            i = j

            
        return res