class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## RC ##
        ## APPROACH : DP ##
        
        dp = [ [0 for j in range(m)] for i in range(n)] 
                
        for i in range(n):
            for j in range(m):
                if( i==0 or j==0 ):                        # base case, for first row and first column, dp will have addition of values, as there is no other way.
                    dp[i][j] = 1
                else:                                       # Logic, find minimum cost to reach that cell from above and left.
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])
        return dp[-1][-1]