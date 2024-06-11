class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair_dict = {}
        result = 0

        for i in range(len(dominoes)):
            temp_pair = (min(dominoes[i]), max(dominoes[i]))

            if temp_pair in pair_dict:
                result += pair_dict[temp_pair]
                pair_dict[temp_pair] += 1
            else:
                pair_dict[temp_pair] = 1

        return result