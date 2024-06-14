class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        max_freq = max(count.values())

        return len([key for key in count if count[key] == max_freq]) * max_freq
    