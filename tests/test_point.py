import unittest
from decimal import Decimal

from geofences.point import Point


class DescribePoint(unittest.TestCase):

    def should_have_abscissa(self):
        self.assertEqual(Point().x, 0)

    def should_have_decimal_abscissa(self):
        self.assertIsInstance(Point().x, Decimal)

    def should_have_ordinate(self):
        self.assertEqual(Point().y, 0)

    def should_have_decimal_ordinate(self):
        self.assertIsInstance(Point().y, Decimal)


class WhenCreatingPoint(unittest.TestCase):

    def should_set_abscissa(self):
        self.assertEqual(Point(x=3).x, 3)

    def should_set_ordinate(self):
        self.assertEqual(Point(y=4).y, 4)

    def should_accept_positional_arguments(self):
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def should_repr(self):
        self.assertEqual(repr(Point(3, 4)), 'Point(3, 4)')


class WhenComputingDistanceBetweenTwoPoints(unittest.TestCase):

    def should_return_distance(self):
        point = Point(9.2, 6)
        self.assertEqual(point.distance(Point(13.2, 9)), 5)


class WhenMovingPoint(unittest.TestCase):

    def setUp(self):
        self.point = Point(9.2, 6)

    def should_update_abscissa(self):
        self.point.move(delta_x=-7)
        self.assertEqual(self.point.x, Decimal('2.2'))

    def should_update_ordinate(self):
        self.point.move(delta_y=7)
        self.assertEqual(self.point.y, 13)
