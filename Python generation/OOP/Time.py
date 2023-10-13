from datetime import time
class Time:
    def __init__(self, hours, minutes):        
        self.set_time(hours, minutes)


    def set_time(self, h, m):
        self._hours = h % 24 + m // 60
        self._minutes = m % 60


    def __str__(self):
        t = time(hour=self._hours, minute=self._minutes)
        return t.strftime("%H:%M")


    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self._hours + other._hours, self._minutes + other._minutes)
        return NotImplemented


    def __iadd__(self, other):
        if isinstance(other, Time):
            self.set_time(self._hours + other._hours, self._minutes + other._minutes)
            return self
        return NotImplemented


# TEST_1:
time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

# TEST_2:
time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

# TEST_3:
time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)

# TEST_4:
time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1 + time2)

# TEST_5:
t = Time(13, 0)
print(t)
id1 = id(t)

t += Time(2, 30)
id2 = id(t)
print(t)
print(id1 == id2)

# TEST_6:
t = Time(13, 0)
times = [(68, 74), (74, 63), (82, 77), (97, 91), (42, 42), (28, 69), (26, 97), (88, 84), (50, 57), (95, 6), (100, 72),
         (18, 17), (76, 38), (9, 5), (65, 11), (16, 9), (56, 64), (57, 93), (35, 22), (57, 68), (100, 95), (6, 59),
         (34, 97), (55, 88), (69, 95), (50, 70), (38, 68), (19, 74), (79, 28), (42, 45), (34, 74), (27, 89), (74, 17),
         (59, 35), (83, 65), (50, 18), (82, 62), (34, 64), (23, 11), (62, 55), (28, 41), (16, 52), (62, 85), (95, 27),
         (56, 59), (45, 31), (82, 39), (45, 22), (22, 39), (28, 78), (68, 72), (97, 22), (68, 45), (6, 19), (62, 69),
         (17, 29), (53, 86), (44, 52), (70, 68), (6, 33), (83, 89), (96, 66), (7, 40), (68, 68), (63, 77), (48, 35),
         (68, 40), (13, 57), (55, 94), (10, 97), (41, 90), (72, 6), (80, 69), (69, 90), (53, 94), (65, 40), (73, 60),
         (99, 13), (32, 95), (65, 75), (79, 5), (11, 58), (41, 49), (88, 66), (13, 43), (88, 23), (67, 64), (65, 9),
         (90, 91), (26, 21), (77, 84), (71, 36), (59, 73), (41, 23), (86, 22), (90, 24), (67, 50), (5, 9), (12, 29),
         (17, 6)]

for hour, minute in times:
    new_time = t + Time(hour, minute)
    print(new_time)

# TEST_7:
t = Time(40, 80)
print(t.__add__([]))
print(t.__iadd__('bee'))

# TEST_8:
t = Time(22, 0)
t += Time(3, 0)
print(t)

# TEST_9:
t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)