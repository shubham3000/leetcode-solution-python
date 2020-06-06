class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (len(matrix)==0):
            return 0
        
        m=len(matrix)
        n=len(matrix[0])
        
        count=[[0]*(n+1) for j in range(m+1)]
        
        area=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (matrix[i-1][j-1]=="1"):
                    count[i][j]=min(count[i-1][j],count[i][j-1],count[i-1][j-1])+1
                    area=max(area,count[i][j])
                    
        return area*area