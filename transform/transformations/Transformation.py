import numpy as np
from matplotlib import pyplot as plt
from transformations.Point2D import Point2D
from transformations.Translate import Translate
from transformations.Rotate import Rotate


class Transformation:
    """ This class creates a Transformation object that requires Translation matrix and a Rotation matrix to calculate the transfomation matrix. 
    This class only defines the '*' operator to apply the transformation to a 2D point and to other Transformations """
    def __init__(self, translation, rotation):
        self.translation = translation
        self.rotation = rotation
        self.matrix = self.rotation.matrix @ self.translation.matrix

    def __mul__(self, point):
        if isinstance(point, Point2D):
            new_coords = self.matrix @ point.homogeneous
            return Point2D(new_coords[0], new_coords[1])
        elif isinstance(point, Transformation):
            new_matrix = self.matrix @ point.matrix
            new_translation = Translate(new_matrix[0, 2], new_matrix[1, 2])
            new_rotation = Rotate(np.arctan2(new_matrix[1, 0], new_matrix[0, 0]))
            return Transformation(new_translation, new_rotation)
        return NotImplemented

    def __repr__(self):
        return f"Transformation(translation={self.translation}, rotation={self.rotation})"
