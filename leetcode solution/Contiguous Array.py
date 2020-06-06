class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict={}
        currsum=0
        count=0
        for i in range(len(nums)):
            currsum += (-1 if (nums[i] == 0) else nums[i]) 
           
            if currsum==0:
                count=i+1
            if currsum in dict:
                count=max(count,i-dict[currsum])
            else:
                dict[currsum]=i
                
        return count