class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target or nums[i]> target:      
                return i                                #return the positon of element
        return len(nums)                                #return the last position if it is out of the list