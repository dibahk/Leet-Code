class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        len_a = len(a)
        len_b = len(b)
        carrier = '0'
        while len_a > 0 and len_b > 0:
            # To find the last digit
            len_a -= 1
            len_b -= 1
            if a[len_a] == '1' and b[len_b] == '1':
                if carrier == '1':
                    ans.insert(0, "1")
                    
                else:
                    ans.insert(0, '0')
                    
                    
                carrier = '1'
            if ((a[len_a] == '0') and (b[len_b] == '1')) or (a[len_a] == '1' and b[len_b] == '0'):
                if carrier == '1':
                    ans.insert(0, "0")
                    carrier = "1"
                    
                else:
                    ans.insert(0, "1")
                    carrier = "0"
                    
            if a[len_a] == '0' and b[len_b] == '0':
                if carrier == '1':
                    ans.insert(0, "1")
                    
                else:
                    ans.insert(0, '0')
                    
                carrier = '0'
        
        
        while len_a > 0:
            len_a -= 1
            # print(f"len a: {i}")
            if a[len_a] == '1':
                if carrier == '1':
                    ans.insert(0, '0')
                    carrier = '1'
                    
                        
                else:
                    ans.insert(0, '1')
                    carrier = '0'
                    
            else:
                if carrier == '1':
                    ans.insert(0, '1')
                    
                else:
                    ans.insert(0, '0')
                    
                carrier = '0'
                
        
        while len_b > 0:
            len_b -= 1
            if b[len_b] == '1':
                if carrier == '1':
                    ans.insert(0, '0')
                    carrier = '1'
                else:
                    ans.insert(0, '1')
                    carrier = '0'
            else:
                if carrier == '1':
                    ans.insert(0, '1')
                else:
                    ans.insert(0, '0')
                carrier = '0'
    
        if len_a <= 0 and len_b <= 0:
            if carrier == "1":
                ans.insert(0, '1')
                
        return "".join(ans)
        
        

                            

            
                                    

