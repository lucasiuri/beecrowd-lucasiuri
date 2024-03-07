# https://judge.beecrowd.com/en/problems/view/1027

# The task is simple. Through some critical points in 2D, you have 
# to draw a wave like curve. Your goal is to include as many points 
# as possible.

# There will be an imaginary line y = a, which we call the major axis for the curve.
# All the points on the curve should have different x coordinates. 
# Their y coordinates should be of form a-1 or a+1.


# Two consecutive points on the curve should have a difference of 
# 2 in their y coordinate.

# Input
# There will be no more than 222 test cases. Each test case starts 
# with an integer N, the number of points in the test case. In the next 
# N lines, there will be N pair of integers giving the x and y coordinate 
# of the points. There will be no more than 1000 points in each test case. 
# All coordinates are integers -- they'd fit in a signed 2 byte integer 
# data type. The data must be read of default input.

# Output
# For each test case print a number -- the maximum number of critical points 
# that can be included in a curve drawn from the given points.

from collections import defaultdict

def compare_points(x1, x2):
    if x1 and not x2:
        return 1
    if not x1:
        return 0
    if x1[0] == x2[0]:
        return 1 + compare_points(x2[1:], x1[1:])
    if x1[0] < x2[0]:
        return 1 + compare_points(x2, x1[1:])
    return compare_points(x1, x2[1:])

while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    y_dict = defaultdict(list)
    curve_points = []
    for _ in range(n):
        x, y = map(int, input().split())
        y_dict[y].append(x)
    for y, x_above in y_dict.items():
        x_below = y_dict.get(y-2, [])
        curve_points.append(compare_points(sorted(x_above), sorted(x_below)))
        curve_points.append(compare_points(sorted(x_below), sorted(x_above)))
    print(max(curve_points))


