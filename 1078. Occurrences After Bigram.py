class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        l = text.split(" ")
        ans = []
        ln = len(l) - 2
        for i in range(ln):
            if (l[i] == first) and l[i+1] == second:
                ans.append(l[i+2])
        return ans


        
