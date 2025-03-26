class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = nums[i-1] *2
                nums[i] = 0
        num_0 = 0
        num_1 = 0
        i = 0
        n = len(nums)
        while num_1 + num_0 < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                num_0 += 1
            else:
                i += 1
                num_1 += 1
        return nums
