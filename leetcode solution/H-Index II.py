"""Explanation:
I will break this down in to two cases.

Case 1：If n-mid==citations[mid]:
We cannot increase the h-index anymore. (If we increase it by 1, the citation before will be excluded, and the number of 
citations>=h-index will definitely be less than h-index)

Case 2: We exit the binary search without hitting the n-mid==citations[mid] condition：
We know that the binary search will stop at the index where citations[low]<h-index< citations[low+1], the maximum h_index possible 
will be the length of citations[low+1:].
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        if n==0:
            return 0
        
        low=0
        high=n
        while high>low:
            mid=(low+high)//2
            if n-mid==citations[mid]:
                return n-mid
            elif n-mid>citations[mid]:
                low=mid+1
            else:
                high=mid
        return n-low
