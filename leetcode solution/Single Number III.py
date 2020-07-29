class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=set()
        b=set()
        for i in nums:
            if i not in a:
                a.add(i) 
            else:
                b.add(i) 
        return (a.difference(b))
		
		
		
"""
Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

"""