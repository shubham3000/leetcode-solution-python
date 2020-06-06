class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        
        while len(stones)>1:
            stones.sort()
            s1,s2=stones[-1],stones[-2]
            if s1==s2:
                stones.pop(-1)
                stones.pop(-1)
            else:
                s1= abs(s1-s2)
                stones.pop(-1)
                stones[-1]=s1
                
        if len(stones):
            return stones[-1]
        else:
            return 0