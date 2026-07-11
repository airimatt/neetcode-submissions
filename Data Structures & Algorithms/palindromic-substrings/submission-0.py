class Solution:
    def countSubstrings(self, s: str) -> int:

        def check(word):
            if word == word[::-1]:
                return 1
            else:
                return 0
        
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                # print(s[i:j + 1])
                res += check(s[i:j + 1])
        
        return res
                

        