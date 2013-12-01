"""geofences.point"""
import math
from decimal import Decimal


class Point(object):
    """A point in 2-D Euclidean space."""
    def __init__(self, x=0, y=0):
        self.x = Decimal(str(x))
        self.y = Decimal(str(y))

    def distance(self, other):
        """
        Return the Euclidean distance between this point and the `other` point.

        """
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return math.hypot(delta_x, delta_y)

    def move(self, delta_x=0, delta_y=0):
        """
        Move the point by `delta_x` horizontally and `delta_y` vertically.

        """
        self.x += Decimal(str(delta_x))
        self.y += Decimal(str(delta_y))

    def __repr__(self):
        return '{0.__class__.__name__}({0.x}, {0.y})'.format(self)

    def __eq__(self, other):
        return self.distance(other) == 0
