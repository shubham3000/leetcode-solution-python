#using bubble sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
					
					
					
# Dutch national flag problem.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        # pointers to keep track of where the current sorting is
        i, left, right = 0, 0, len(nums)-1
        while i <= right:
            if nums[i] == 0:
                # swap left
                nums[left], nums[i] = nums[i], nums[left]
                left += 1; i += 1
            elif nums[i] == 2:
                # swap right
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else: i += 1