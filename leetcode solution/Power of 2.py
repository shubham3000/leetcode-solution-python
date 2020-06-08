"""Another solution is to keep dividing the number by two, i.e, do n = n/2 iteratively. In any iteration, if n%2 becomes non-zero
and n is not 1 then n is not a power of 2. If n becomes 1 then it is a power of 2."""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while(n!=1):
            if (n%2 !=0):
                return False
            n=n//2
        return True