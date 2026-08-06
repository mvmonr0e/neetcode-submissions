class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            temp = str(len(s)) + '!' + s
            encoded += temp

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        res = ''
        while i < len(s):
            j = i
            while s[j] != '!':
                j += 1
            length = int(s[i:j])
            res = s[j + 1 : j + length + 1]
            decoded.append(res)

            i = j + length + 1

        return decoded
            
