class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        dic = {}
        if len(pattern) != len(l):
            return False
        j = 0
        for i in pattern:
            if i in dic.keys():
                if dic[i] != l[j]:
                    return False
            elif l[j] in dic.values():
                return False
            else:
                dic[i] = l[j]
                print(dic[i])
            j += 1
        return True

        
