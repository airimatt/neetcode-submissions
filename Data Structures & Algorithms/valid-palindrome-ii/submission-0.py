class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(word):
            return word == word[::-1]

        for i in range(len(s)):
            if check(s[:i] + s[i + 1:]):
                return True
        
        return False
        