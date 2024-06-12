class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remaining = numBottles
        result  = 0
        while remaining >= numExchange:
            result += remaining // numExchange * numExchange
            remaining = remaining // numExchange + remaining % numExchange
        result += remaining
        return result
