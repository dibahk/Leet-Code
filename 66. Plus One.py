class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        right = len(digits) - 1
        while flag:
            digits[right] += 1
            if digits[right] > 9:
                digits[right] -= 10
                if right == 0:
                    digits.insert(0,1)
                    return digits
                right -= 1
            else:
                return digits
            
