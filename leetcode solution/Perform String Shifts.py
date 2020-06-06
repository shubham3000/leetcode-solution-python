class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction,amount in shift:
            amount=amount%len(s)
            if direction==0:
                s=s[amount:]+s[:amount]
            else:
                s=s[-amount:]+s[:-amount]
        return s