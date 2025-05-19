class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        
    def __add__(self, other):
        total_sec = self.second + other.second
        total_min = self.minute + other.minute + total_sec // 60
        total_hour = self.hour + other.hour + total_min // 60
        total_sec = total_sec % 60
        total_min = total_min % 60
        return f"You studied for {total_hour} hours, {total_min} minutes, and {total_sec} seconds."

t1 = Time(2, 45, 50)
t2 = Time(1, 20, 30)
print(t1 + t2)