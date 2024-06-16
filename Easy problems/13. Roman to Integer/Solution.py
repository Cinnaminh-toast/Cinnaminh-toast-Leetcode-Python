class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0

        for i in range(len(s) - 1):
            if conversion_dict[s[i]] < conversion_dict[s[i+1]]:
                result -= conversion_dict[s[i]]
            else:
                result += conversion_dict[s[i]]
        result += conversion_dict[s[-1]]
        return result
        