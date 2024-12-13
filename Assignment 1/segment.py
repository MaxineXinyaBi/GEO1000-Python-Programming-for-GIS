# GEO1000 - Assignment 1
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350 ,6235379

from math import sqrt, acos, pi

def distance(x1, y1, x2, y2):
    """the function is to use cartesian formula to calculate distance from point A(x1,y1) to point B(x2,y2)"""
    cartesian_dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return cartesian_dist


def heron(a, b, c):
     """the function is to use heron formula to calculate the area of the triangle"""
     s =  (a + b + c) / 2
     area =  sqrt(s * (s - a) * (s - b) * (s - c))
     return area


def angle(a, b, c):
    """the function is to use acos to calculate the angle"""
    if a == 0 or b == 0 or c == 0:
        return 0
    gama_angle = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return gama_angle


def segment_point_dist(s1x, s1y, s2x, s2y, px, py):
    """the function is to calculate the distance between a point to a line"""
    s1s2 = distance(s1x, s1y, s2x, s2y)
    s1p = distance(s1x, s1y, px, py)
    s2p = distance(s2x, s2y, px, py)

    angle_a = angle(s1s2, s1p, s2p) * 180 / pi
    angle_b = angle(s2p, s1s2, s1p) * 180 / pi

    # if both angle a and b is less than 90 degree, then use the area method
    if angle_a < 90 and angle_b < 90:
        area = heron(s1s2,s1p, s2p)
        height = 2 * area / s1s2
    # if angle a or b is bigger than or equal to 90 degree or points are on the same line
    # then the minimum distance method
    else:
        height = min(s1p, s2p)
    return height


print(segment_point_dist(0, 0, 10, 0, 5, 10))
print(segment_point_dist(0, 0, 10, 0, 20, 0))
print(segment_point_dist(0, 0, 10, 0, 0, 0))
print(segment_point_dist(0, 0, 10, 0, 5, 0))
print(segment_point_dist(0, 0, 10, 10, 0, -12))
