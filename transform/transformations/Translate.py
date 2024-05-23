import numpy as np 
from matplotlib import pyplot as plt
from transformations.Point2D import Point2D

class Translate:
    """ This class defines tranlation of the points in the x-direction and y-direction using a 3x3 translation matrix to perform the operation. 
    It also defines the following operators '+' and '-' with other Translation objects as well as the '*' to translate 2D points. """
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])

    def __add__(self, other):
        if isinstance(other, Translate):
            return Translate(self.dx + other.dx, self.dy + other.dy)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Translate):
            return Translate(self.dx - other.dx, self.dy - other.dy)
        return NotImplemented

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.homogeneous
            return Point2D(new_coords[0], new_coords[1])
        return NotImplemented

    def __repr__(self):
        return f"Translate(dx={self.dx:.2f}, dy={self.dy:.2f})"