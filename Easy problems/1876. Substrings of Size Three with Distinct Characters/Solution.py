class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def check_goodness(s):
            for i in range(2):
                if s[i] in s[i+1:]:
                    return False
            return True
        result = 0
        for i in range(len(s) - 3 + 1):
            result += 1 if check_goodness(s[i:i+3]) else 0

        return result
