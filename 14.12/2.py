from math import sin, cos
x = 2.0
while 5 * sin(3 * x) - 3 * cos(7 * x) <= 0:
    x += 0.00001
    x = round(x, 5)
print('{:.5f}'.format(x))