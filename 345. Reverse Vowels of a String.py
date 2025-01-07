class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = []
        for i in l:
            if i in vowels:
                v.append(i)
        v.reverse()
        ans = ""
        for i in range(len(l)):
            if l[i] in vowels:
                ans += v.pop(0)
            else:
                ans += l[i]
        return ans
