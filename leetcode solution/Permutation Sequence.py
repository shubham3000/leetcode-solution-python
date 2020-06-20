from itertools import permutations           #using library function
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=[]
        for i in range(1,n+1):
            a.append(i)               
        
        perm = permutations(a)       #using function
        res=[]
        for i in list(perm):
            res.append(i)
        out=res[k-1]                     #store k-1th position
        return (''.join(str(v) for v in out))        #return in string output 
