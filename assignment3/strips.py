# GEO1000 - Assignment 3
# Authors: Xinya Bi; Xu Wang
# Studentnumbers:6195350; 6235379


from geometry import Point, Rectangle


class Strip:
    def __init__(self, rectangle):
        """Constructor. Inits a Strip instance with a Rectangle describing 
        its shape and an empty points list.
        """
        self.rect = rectangle
        self.points = []


class StripStructure:
    def __init__(self, extent, no_strips):
        """Constructor. Inits a StripStructure instance with the correct
        number of Strip instances and makes sure that the domain is 
        correctly divided over the strips.
        """
        self.strips = []
        # Extend this method,
        # so that the right number of strip objects (with the correct extent)
        # are appended to the strips list
        # assert the shape of the extent is a rectangle
        assert isinstance(extent, Rectangle)
        self.extent = extent
        self.no_strips = no_strips
        # calculate the width of each strip
        strip_width = extent.width() / no_strips

        # use rectangle class to build and append strip into strips list
        for i in range(no_strips):
            strip_ll_x = extent.ll.x + i * strip_width
            strip_ur_x = strip_ll_x +  strip_width
            strip_rectangle = Rectangle(Point(strip_ll_x,extent.ll.y),Point(strip_ur_x, extent.ur.y))
            new_strip = Strip(rectangle=strip_rectangle)
            self.strips.append(new_strip)


    def find_overlapping_strips(self, shape):
        """Returns a list of strip objects for which their rectangle intersects 
        with the shape given.

        Returns - list of Strips
        """
        overlapped_strips = []
        for strip in self.strips:
            if strip.rect.intersects(shape):
                overlapped_strips.append(strip)
        return overlapped_strips


    def query(self, shape):
        """Returns a list of points that overlaps the given shape.

        For this it first finds the strips that overlap the shape,
        using the find_overlapping_strips method.

        Then, all points of the selected strips are checked for intersection
        with the query shape.

        Returns - list of Points
        """
        overlapped_points = []
        for overlapped_strip in self.find_overlapping_strips(shape):
            for point in overlapped_strip.points:
                if shape.intersects(point):
                    overlapped_points.append(point)
        return overlapped_points

    def append_point(self, pt):
        """Appends a point object to the list of points of the correct strip
        (i.e. the strip the Point intersects).

        For this it first finds the strips that overlap the point,
        using the find_overlapping_strips method.

        In case multiple strips overlap the point, the point is added
        to the strip with the left most coordinate.

        Returns - None
        """
        assert isinstance(pt, Point)
        overlapped_strips = self.find_overlapping_strips(pt)
        # make sure it falls into the left most strip
        left_most_strip = overlapped_strips[0]
        left_most_strip.points.append(pt)


    def print_strip_statistics(self):
        """Prints:
        * how many strips there are in the structure

        And then, for all the strips in the structure:
        * an id (starting at 1),
        * the number of points in a strip, 
        * the lower left point of a strip and 
        * the upper right point of a strip.

        Returns - None
        """
        print(f"Strip Statistics: The number of points in the structure: {self.no_strips}")
        for index, strip in enumerate(self.strips, start=1):
            print(f"ID:{index}, Number of Points:{len(strip.points)}, The lower Point:{strip.rect.ll}, The upper point:{strip.rect.ur}")

    def dumps_strips(self):
        """Dumps the strips of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.

        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start=1):
            t = "{0};{1}\n".format(i, strip.rect)
            lines += t
        return lines

    def dumps_points(self):
        """Dumps the points of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.

        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start=1):
            for pt in strip.points:
                t = "{0};{1}\n".format(i, pt)
                lines += t
        return lines

