class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minutes_angle = minutes * 6

        angle = abs(hour_angle - minutes_angle)

        return min(angle, 360 - angle)
