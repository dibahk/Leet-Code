class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s = list(s)
        t = list(t)
        for char in s:
            if len(t)== 0:
                break
            if char == t[0]:
                t.pop(0)
        return len(t)
        
