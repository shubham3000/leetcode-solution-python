class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        start = 0
        end = n - 1
        while start + 1 < end :
            mid = (start+end)//2
            if  nums[mid]  == target:
                return mid
        
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
