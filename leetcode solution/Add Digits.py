import math
class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while(num>0 or sum>9):
            if (num==0):
                num=sum
                sum=0
            sum += (num%10)
            num //= 10
        return (sum)
		
		
"""
Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""