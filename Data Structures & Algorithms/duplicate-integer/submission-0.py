class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        converted = set(nums)
        return (len(converted) != len(nums))