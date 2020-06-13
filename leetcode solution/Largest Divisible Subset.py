class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
			
        nums.sort()
        n=len(nums)
        dp=[1 for i in range(n)]           # dp[i] is going to store size of largest divisible subset beginning with a[i]. 
    
        for i in range(1,n):                       # Find all multiples of nums[i] and consider the multiple  
            for j in range(i-1,-1,-1):               # that has largest subset beginning with it. 
                if (nums[i] % nums[j] == 0):
                    dp[i]=max(dp[i],dp[j]+1)
        
        m = max(dp)             # Return maximum value from dp[]  
        val = 1
    
        res = []
        i = 0
        while val <= m and i < n:       #store all elements in new list
            if dp[i] == val:
                res.append(nums[i])
                val+=1
            i+=1
    
        return res
                