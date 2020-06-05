Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7

Explanation: Because the path 1--->3--->1--->1--->1 minimizes the sum.

python solution

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)== 0 or len(grid[0])==0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if r==c==0:
                    continue
                if r==0: 
                    grid[r][c] = grid[r][c] + grid[r][c-1]  
                elif c==0: 
                    grid[r][c] = grid[r][c] + grid[r-1][c] 
                else: 
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])  
        
        return grid[rows-1][cols-1]