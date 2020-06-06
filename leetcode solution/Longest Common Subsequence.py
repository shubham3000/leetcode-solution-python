class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        count=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    count[i][j]=1+count[i-1][j-1]
                else:
                    count[i][j]=max(count[i-1][j],count[i][j-1])
        return count[m-1][n-1]