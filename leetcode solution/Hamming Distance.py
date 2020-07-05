class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        
        xb = bin(x)[2:].zfill(32)
        yb = bin(y)[2:].zfill(32)
        
        distance=0
        for i in range(32):
            if xb[i] != yb[i]:
                distance += 1
        return distance
		
"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
If the value of the len parameter is less than the length of the string, no filling is done.
EX:
   a = "hello"
   print(a.zfill(10))
   
   output:
        00000hello
"""

"""
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different."""