import unittest

from geofences.circle import Circle
from geofences.geofence import Geofence
from geofences.point import Point
from geofences.user import User


class DescribeGeofence(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(radius=10)
        self.geofence = Geofence(name='Home', boundary=self.circle)

    def should_have_name(self):
        self.assertEqual(self.geofence.name, 'Home')

    def should_have_boundary(self):
        self.assertEqual(self.geofence.boundary, self.circle)


class WhenCreatingGeofence(unittest.TestCase):

    def should_accept_boundary_kwargs(self):
        geofence = Geofence(name='Home', radius=10, center=(4, 5))
        self.assertEqual(geofence.boundary.radius, 10)
        self.assertEqual(geofence.boundary.center, Point(4, 5))


class DescribeGeofenceContains(unittest.TestCase):

    def setUp(self):
        self.geofence = Geofence(name='Home', radius=10, center=(4, 6))

    def should_return_True_if_locatable_is_inside_boundary(self):
        user = User('Daisy', position=(0, 0))
        self.assertTrue(user in self.geofence)

    def should_return_False_if_locatable_is_outside_boundary(self):
        user = User('Daisy', position=(20, -20))
        self.assertFalse(user in self.geofence)

    def should_return_True_if_locatable_is_on_boundary(self):
        user = User('Daisy', position=(14, 6))
        self.assertTrue(user in self.geofence)
