import numpy as np
from matplotlib import pyplot as plt

class Point2D:
    """ This class defines 2D points as homogeneous points . 
    it defines the operation '+' and '-' with other points as well as the logical operators '<' '==' . 
    it also defines the method 'plot()' to plot the points defined in the class."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.homogeneous = np.array([x, y, 1])

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point2D):
            return (self.x, self.y) < (other.x, other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    def plot(self, color='r'):
        plt.scatter(self.x, self.y, c=color)
        plt.text(self.x, self.y, f'({self.x:.2f}, {self.y:.2f})', fontsize=9, ha='right')