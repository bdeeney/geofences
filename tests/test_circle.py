import unittest
from decimal import Decimal

from geofences.circle import Circle
from geofences.point import Point


class DescribeCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(radius=5)

    def should_have_center_point(self):
        self.assertIsInstance(self.circle.center, Point)

    def should_be_centered_on_origin_by_default(self):
        self.assertEqual(self.circle.center, Point(0, 0))

    def should_have_radius(self):
        self.assertIsInstance(self.circle.radius, Decimal)


class WhenCreatingCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(center=Point(-1, 3), radius=5)

    def should_set_radius(self):
        self.assertEqual(self.circle.radius, 5)

    def should_set_center_point(self):
        self.assertEqual(self.circle.center, Point(-1, 3))


class DescribeCircleContains(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(center=(-1, 3), radius=5)

    def should_return_True_when_point_is_inside_circle(self):
        self.assertTrue(Point(2, 4) in self.circle)

    def should_return_False_when_point_is_outside_circle(self):
        self.assertFalse(Point(6, -2) in self.circle)

    def should_return_True_when_point_lies_on_circle(self):
        self.assertTrue(Point(4, 3) in self.circle)
