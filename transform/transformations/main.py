#!/usr/bin/env python3
import numpy as np 
from matplotlib import pyplot as plt
from Transformation import Transformation as tf
from transformations.Point2D import Point2D
from transformations.Translate import Translate
from transformations.Rotate import Rotate

def main():

# Set up the points
    points = [tf.Point2D(2, 4), tf.Point2D(3, 6), tf.Point2D(), tf.Point2D(1, 2)]
    for p in points:
        print(p)

    # Set up the transformations
    t1 = tf.Translate(1, 0)
    r1 = tf.Rotate(np.pi/8)
    T1 = tf.Transformation(t1, r1)
    print(t1, r1, T1)

    # Do operations with points
    points.sort()
    p_total = tf.Point2D()
    for p in points:
        p_total = p_total + p
        print(p)
    print(p_total)

    # Do operations with transformations
    print(t1+t1)
    print(r1+r1)
    for p in points:
        p.plot('r')   # color red
        p_t = t1 * p
        p_t.plot('b') # color blue
        p_r = r1 * p
        p_r.plot('g') # color green
        p_T = T1 * p
        p_T.plot('y') # color yellow

    plt.axis('equal')   
    plt.show()