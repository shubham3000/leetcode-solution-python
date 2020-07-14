class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if (hour < 0 or minutes < 0 or hour > 12 or minutes > 60): 
            return 0
        
        minute_angle = minutes * 6
        hour_angle = (hour + (minutes / 60)) * 30            # calculate hour angle by adding minutes into hour
        
        angle = min(360 - abs(hour_angle - minute_angle), abs(hour_angle - minute_angle))          # get absolute difference between angles
        return (angle)
        