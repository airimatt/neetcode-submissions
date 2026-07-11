class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            shift = int(s[start:i])
            i += 1
            res.append(s[i:i + shift])
            i += shift
        
        return res
            
