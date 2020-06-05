Leetcode june week1 challenge Random Pick with Weight

Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a 
function pickIndex whichrandomly picks an index in proportion to its weight.

Note:

1)1 <= w.length <= 10000
2)1 < = w[i] < = 10^5
3)pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. 
pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

python solution

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