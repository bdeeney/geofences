"""geofences.circle"""
from copy import deepcopy
from decimal import Decimal

from geofences.point import Point


class Circle(object):
    """A circle in 2-D Euclidean space."""
    def __init__(self, radius, center=(0, 0)):
        self.radius = Decimal(radius)
        if isinstance(center, tuple):
            self.center = Point(*center)
        else:
            self.center = deepcopy(center)

    def __contains__(self, point):
        """Whether the circle contains the given `point`.

        A point on the circle is considered to be contained by the circle.

        """
        return self.center.distance(point) <= self.radius

    def __eq__(self, other):
        return other.radius == self.radius and other.center == self.center
