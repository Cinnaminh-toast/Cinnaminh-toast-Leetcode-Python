class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        k = int(len(nums) / 2)
        result = len(nums) % 2
        arr1 = nums[:k]
        arr2 = nums[-k:]

        pointer_1, pointer_2 = 0, 0

        while pointer_1 < k and pointer_2 < k:
            if arr1[pointer_1] < arr2[pointer_2]:
                pointer_1 += 1
                pointer_2 += 1
            else:
                pointer_2 += 1
                result += 1

        result += k - pointer_1
        return result
