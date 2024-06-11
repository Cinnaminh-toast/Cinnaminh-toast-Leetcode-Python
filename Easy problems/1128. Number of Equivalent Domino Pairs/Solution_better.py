class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cache = {}
        result = 0

        for a, b in dominoes:
            pair = (a, b) if a < b else (b,a)
            # Clean way to update dict
            cache[pair] = cache.get(pair, 0) + 1

        result = sum([value * (value - 1) // 2 for value in cache.values()])

        return result   