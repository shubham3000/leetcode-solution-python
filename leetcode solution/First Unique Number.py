class FirstUnique:

    def __init__(self, nums: List[int]):
        self.deque=collections.deque()
        self.output={}
        
        for i in nums:
            self.add(i)
            
    def showFirstUnique(self) -> int:
        while (self.deque and self.output[self.deque[0]] !=1):
            self.deque.popleft()
        if(len(self.deque)==0):
            return -1
        
        return self.deque[0]

    def add(self, value: int) -> None:
        if value in self.output:
            self.output[value] +=1
        else:
            self.output[value]=1
        self.deque.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)