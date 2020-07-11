from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        a=[]
        for i in range(n+1):
            for c in list(combinations(nums,i)):
                a.append(c)
        return (a)