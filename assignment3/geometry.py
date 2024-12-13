# GEO1000 - Assignment 3
# Authors: Xinya Bi; Xu Wang
# Studentnumbers:6195350; 6235379

import math

# __all__ leaves out _test method and only makes
# the classes available for "from geometry import *":
__all__ = ["Point", "Circle", "Rectangle"]


class Point:

    def __init__(self, x, y):
        """Constructor. 
        Takes the x and y coordinates to define the Point instance.
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Returns WKT String "POINT (x y)".
        """
        return f"POINT ({self.x}, {self.y})"

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        returns - True / False
        """
        # point intersect with point
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False


    def distance(self, other):
        """Returns cartesian distance between self and other Point
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


class Circle:

    def __init__(self, center, radius):
        """Constructor. 
        Takes the center point and radius defining the Circle.
        """
        assert radius > 0
        assert isinstance(center, Point)
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """Returns WKT str, discretizing the boundary of the circle 
        into straight line segments
        """
        N = 400
        step = 2 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius,
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON (({0}))".format(coordinates)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        Returns - True / False
        """
        # point intersect with circle
        if isinstance(other, Point):
            dis = other.distance(self.center)
            if dis <= self.radius:
                return True
        # circle intersect with circle
        elif isinstance(other, Circle):
            if self.center.distance(other.center) <= self.radius + other.radius:
                return True
        else:
            return False



class Rectangle:

    def __init__(self, pt_ll, pt_ur):
        """Constructor. 
        Takes the lower left and upper right point defining the Rectangle.
        """
        assert isinstance(pt_ll, Point)
        assert isinstance(pt_ur, Point)
        self.ll = pt_ll
        self.ur = pt_ur

    def __str__(self):
        """Returns WKT String "POLYGON ((x0 y0, x1 y1, ..., x0 y0))"
        """
        return f"POLYGON ({self.ll.x} {self.ll.y}, {self.ur.x} {self.ll.y}, {self.ur.x} {self.ur.y}, {self.ll.x} {self.ur.y}, {self.ll.x} {self.ll.y})"

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle

        Returns - True / False
        """
        # point intersect with rectangle
        if isinstance(other, Point):
            return self.ll.x <= other.x <= self.ur.x and self.ll.y <= other.y <= self.ur.y
        # rectangle intersect rectangle
        elif isinstance(other, Rectangle):
            x_overlap = self.ll.x <= other.ur.x and other.ll.x <= self.ur.x
            y_overlap = self.ll.y <= other.ur.y and other.ll.y <= self.ur.y
            return x_overlap and y_overlap
        # rectangle intersect circle
        elif isinstance(other, Circle):
            # create additional rectangles
            top_rec = Rectangle(
                Point(self.ll.x, self.ur.y),
                Point(self.ur.x, self.ur.y + other.radius)
            )
            bottom_rec = Rectangle(
                Point(self.ll.x, self.ll.y - other.radius),
                Point(self.ur.x, self.ll.y)
            )
            left_rec = Rectangle(
                Point(self.ll.x - other.radius, self.ll.y),
                Point(self.ll.x, self.ur.y)
            )
            right_rec = Rectangle(
                Point(self.ur.x, self.ll.y),
                Point(self.ur.x + other.radius, self.ur.y)
            )

            # create additional circles
            top_left_circle = Circle(Point(self.ll.x, self.ur.y), other.radius)
            top_right_circle = Circle(Point(self.ur.x, self.ur.y), other.radius)
            bottom_left_circle = Circle(Point(self.ll.x, self.ll.y), other.radius)
            bottom_right_circle = Circle(Point(self.ur.x, self.ll.y), other.radius)

            # check intersection
            # point intersect with original rectangle
            if self.intersects(other.center):
                return True
            # point intersect with four rectangles
            if (top_rec.intersects(other.center) or bottom_rec.intersects(other.center) or
                    left_rec.intersects(other.center) or right_rec.intersects(other.center)):
                return True
            # point intersect with 4 circles
            if (top_left_circle.intersects(other.center) or top_right_circle.intersects(other.center) or
                    bottom_left_circle.intersects(other.center) or bottom_right_circle.intersects(other.center)):
                return True
        else:
            return False


    def width(self):
        """Returns the width of the Rectangle.

        Returns - float
        """
        return self.ur.x - self.ll.x

    def height(self):
        """Returns the height of the Rectangle.

        Returns - float
        """
        return self.ur.y - self.ll.y


def _test():
    """Test whether your implementation of all methods works correctly.
    """
    pt0 = Point(0, 0)
    pt1 = Point(0, 0)
    pt2 = Point(10, 10)
    assert pt0.intersects(pt1)
    assert pt1.intersects(pt0)
    assert not pt0.intersects(pt2)
    assert not pt2.intersects(pt0)

    c = Circle(Point(-1, -1), 1)
    r = Rectangle(Point(0, 0), Point(10, 10))
    assert not c.intersects(r)

    # Extend this method to be sure that you test all intersects methods!
    # Read Section 16.5 of the book if you have never seen the assert statement
    c2 = Circle(Point(-1, -1), 2)
    r2 = Rectangle(Point(0, 0), Point(10, 5))
    # test rectangle intersect rectangle
    assert r.intersects(r2)
    # test point intersect rectangle
    assert r.intersects(pt0)
    assert r2.intersects(pt0)
    assert r.intersects(pt2)
    assert not r2.intersects(pt2)
    # test point intersect circle
    assert not c.intersects(pt0)
    assert not c.intersects(pt1)
    assert not c.intersects(pt2)
    assert not c2.intersects(pt2)
    assert c2.intersects(pt0)
    assert c2.intersects(pt1)
    # test circle intersect circle
    assert c.intersects(c2)


if __name__ == "__main__":
    _test()
