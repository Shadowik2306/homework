from math import sin, cos
x = 1.0
while 2 * sin(4 * x) - 5 * cos(7 * x) <= 0:
    x += 0.00001
    x = round(x, 5)
print('{:.5f}'.format(x))