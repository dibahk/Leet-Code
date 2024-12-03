class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for end in range(l, len(haystack)+1):
            if haystack[end-l:end] == needle:
                return end - l
        return -1
        
