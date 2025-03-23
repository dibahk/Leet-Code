class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = sorted(nums)
        # i = 1
        # while i < len(nums):
        #     if s[i] != s[i-1]:
        #         i += 1
        #     else:
        #         return True
        # return False
        s = set(nums)
        return len(s) != len(nums)
        
