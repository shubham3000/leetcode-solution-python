class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
		a=[]
        b=[]
        for i in nums:
            if i not in a:
				a.append(i)
            else:
                b.append(i)
        return (b[0])
		
		
#Another type
		
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return (nums[i])