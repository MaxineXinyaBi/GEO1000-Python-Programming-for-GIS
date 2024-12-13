# GEO1000 - Assignment 3
# Authors: Xinya Bi; Xu Wang
# Studentnumbers:6195350; 6235379

from geometry import Point, Rectangle, Circle
from strips import StripStructure
import os

def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.

    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.

    Returns - None or a StripStructure instance
    """

    with open(file_nm, 'r') as f:
        uncommented_lines = [line for line in f.readlines() if not line.startswith('#')]
        if not uncommented_lines:
            return None
        bbox = uncommented_lines[0].strip().split(' ')
        if len(bbox) != 4:
            return None
        extent = Rectangle(Point(bbox[0], bbox[1]), Point(bbox[2], bbox[3]))
        # create a strip structure
        strip_structure = StripStructure(extent=extent, no_strips=no_strips)
        # deal with point data
        for line in uncommented_lines[1:]:
            point = line.strip().split(' ')
            if len(point) == 2:
                strip_structure.append_point(Point(point[0], point[1]))
        return strip_structure



def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.

    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dumps_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dumps_points())


def _test():
    """You can use this function to test whether 
    the read and dump functions work correctly.
    """
    structure = read('points2.txt',5)
    if structure is None:
        print("Test Failed.There is no structure")
    if structure.extent.ll.x != 0 or structure.extent.ll.y != 0 or structure.extent.ur.x != 10 or structure.extent.ur.y != 10:
        print("Test Failed. Not a rectangle.")

    # test dumping
    dump(structure, "test_strips.wkt", "test_points.wkt")
    with open("test_strips.wkt", "r") as f:
        strips_content = f.read().splitlines()
    with open("test_points.wkt", "r") as f:
        points_content = f.read().splitlines()
    if not strips_content or not points_content:
        print("Test Failed. The test points and strips are empty")

    if len(strips_content) != 6:
        print(f"Test Failed. There are supposed to be 5 strips, but got {len(strips_content)}")
    expected_points= 121
    if len(points_content) != expected_points + 1:
        print(f"Test Failed. There are supposed to be {expected_points} points, but got {len(points_content)}")

    os.remove("test_strips.wkt")
    os.remove("test_points.wkt")

    print("All tests passed.")


if __name__ == "__main__":
    _test()
