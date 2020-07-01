class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows=0
        while n>0:
            if n>rows:
                rows+=1 
            else:
                return rows 
            n=n-rows
        return rows 