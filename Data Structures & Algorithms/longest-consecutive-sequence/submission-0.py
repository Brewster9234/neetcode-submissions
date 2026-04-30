class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        clavicular = set(nums)
        longest = 0
        for num in clavicular:
            if (num-1) not in clavicular:
                length = 1
                while num + length in clavicular:
                    length +=1
                longest = max(longest, length)
        return longest


