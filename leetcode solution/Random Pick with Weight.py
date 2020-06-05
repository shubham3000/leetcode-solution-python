class Solution:

    def __init__(self, w: List[int]):
        self.presum=[]
        presum=0
        for weight in w:
            presum += weight
            self.presum.append(presum)
        self.totalsum=presum 
    
    def pickIndex(self) -> int:
        randomnum,l, h = self.totalsum*random.random(), 0, len(self.presum)
        while l < h:
            m = l+(h-l)//2
            if self.presum[m] < randomnum:
                l = m+1
            else: 
                   h = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
