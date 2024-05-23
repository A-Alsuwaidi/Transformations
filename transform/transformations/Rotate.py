import numpy as np 
from matplotlib import pyplot as plt
from transformations.Point2D import Point2D

class Rotate:
    """ This class defines The rotation of a point W.R.T angle theta. the class uses a 3x3 rotation matrix to perform the operation.
     the class considers the following operators '+' and '-' with other Rotation objects as well as the '*' to rotate 2D Points """
    def __init__(self, theta):
        self.theta = theta
        self.matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])

    def __add__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta + other.theta)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta - other.theta)
        return NotImplemented

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.homogeneous
            return Point2D(new_coords[0], new_coords[1])
        return NotImplemented

    def __repr__(self):
        return f"Rotate(theta={self.theta:.2f})"

