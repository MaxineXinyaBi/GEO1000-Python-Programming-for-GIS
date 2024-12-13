# GEO1000 - Assignment 2
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350, 6235379

import math

def distance(p1, p2):
    """Returns Cartesian distance (as float) between two 2D points"""
    x1, y1 = p1
    x2, y2 = p2
    cartesian_dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cartesian_dis


def point_angle_distance(pt, beta, distance):
    """Compute new point that is distance away from pt in direction beta"""
    x1, y1 = pt
    x2 = x1 + distance * math.cos(beta)
    y2 = y1 + distance * math.sin(beta)
    return x2, y2


def absolute_angle(p1, p2):
    """Returns the angle (in radians) between the positive x-axis 
    and the line through two given points, p1 and p2"""
    x1, y1 = p1
    x2, y2 = p2
    angle = math.atan2(y2 -y1, x2-x1)
    return angle

def opposite_edge(p1, p2):
    """Compute and return the edge (as a tuple of two points p3 and p4) 
    parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    # step1: calculate the angle between p1 and p2
    gama = absolute_angle(p1, p2)
    # step2: calculate the distance between p1 and p2
    length = distance(p1, p2)
    # step3: rotate the angle 90 degrees
    new_angle = gama + math.pi / 2
    # step3: calculate x, y for p4
    x4, y4 = point_angle_distance(p1, new_angle, length)
    # step4: calculate x,y for p3
    x3, y3 = point_angle_distance(p2, new_angle, length)
    return (x3, y3), (x4, y4)



def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    x1, y1 = p1
    x2, y2 = p2
    x = x2 - x1
    y = y2 - y1
    x3 = x1 + x * math.cos(alpha) - y * math.sin(alpha)
    y3 = y1 + x * math.sin(alpha) + y * math.cos(alpha)
    return (x3, y3)


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square
    """
    points = [p1, p2, p3, p4, p1]
    points_str = []
    for x, y in points:
        points_str.append(f"{x:.4f} {y:.4f}")
    coor = ', '.join(points_str)
    wkt = f'POLYGON (({coor}))'
    return wkt


def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    print(f"Drawing order {currentorder}: p1={p1}, p2={p2}")
    # step1 construct a square
    p3, p4 = opposite_edge(p1, p2)

    # 2: area calculation
    area = distance(p1, p2) ** 2

    # 3: export the coordinates and area into output file
    with open(filename,'a') as f:
        wkt = as_wkt(p1, p2, p3, p4)
        f.write(f"{wkt};{currentorder};{area:.4f}\n")

    # 4: calculate the split point
    p5 = split_point(p4, p3, alpha)

    # 5 draw left and right trees
    if currentorder < totalorder:
        draw_pythagoras_tree(p4, p5, alpha, currentorder+1, totalorder, filename)
        draw_pythagoras_tree(p5, p3, alpha, currentorder+1, totalorder, filename)


if __name__ == "__main__":
    with open('out.wkt', 'w') as fh:  # 'with' statement closes 
                                      # file automatically
        fh.write("geometry;currentorder;area\n")
    # here the file is thus closed

    draw_pythagoras_tree(p1=(5,0), 
        p2=(6,0), 
        alpha=math.radians(45),
        currentorder=0,
        totalorder=6,
        filename='out.wkt'  # filename, *not* file instance
    )

