from math import sin, cos
x = 1.5
while 3 * sin(8 * x) - 2 * cos(5 * x) <= 0:
    x += 0.00001
    x = round(x, 5)
print('{:.5f}'.format(x))