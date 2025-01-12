class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = n1 + n2
        i = 0
        j = 0
        ans = ""
        while j < n:
            if i < n1:
                ans += word1[i]
                j += 1
            if i < n2:
                ans += word2[i]
                j += 1
            i += 1
        return ans
