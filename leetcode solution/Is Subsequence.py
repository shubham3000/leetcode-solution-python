"""Define length of two strings.
 while loop check the index of s1 and s2.
 if s[i]==t[j] then index of i increases by 1 otherwise index of j will increase by 1."""
 
 class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=len(s)
        s2=len(t)
        
        i=0
        j=0
        
        while i<s1 and j<s2:
            if s[i]==t[j]:
                i+=1
            j+=1
        if i==s1:
            return True