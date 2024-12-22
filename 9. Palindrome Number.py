class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        print(int(len(x)/2))
        for i in range(int(len(x)/2)):
            if x[i] != x[-1-i]:
                return False
        return True
