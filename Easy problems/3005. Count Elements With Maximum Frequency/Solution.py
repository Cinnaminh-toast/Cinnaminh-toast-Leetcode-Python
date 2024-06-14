class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict_track_freq = {}

        for num in nums:
            dict_track_freq[num] = dict_track_freq.get(num, 0) + 1

        max_freq = max(dict_track_freq.values())
        
        return len([i for i in dict_track_freq.keys() if dict_track_freq[i] == max_freq]) * max_freq
    