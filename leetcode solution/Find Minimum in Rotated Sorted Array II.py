class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarysearch(l, h):
            while l < h:
                mid = (l + h)//2
                val = nums[mid]
                if val < nums[h]:
                    h = mid
                elif val > nums[h]: 
                    l = mid + 1
                else:
                    return min(binarysearch(l, mid), binarysearch(mid+1, h))
            return nums[l]
        return binarysearch(0, len(nums) - 1) 
		
		
		
		
"""		
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.


Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
"""